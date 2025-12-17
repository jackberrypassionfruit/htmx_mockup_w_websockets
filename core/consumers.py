import json

from django.template.loader import render_to_string
from channels.generic.websocket import WebsocketConsumer
from django.utils import timezone
from django.db.utils import IntegrityError
from django.db.models import Count, Q, Max
from django.contrib import messages
from asgiref.sync import async_to_sync

from .models import SerializeMaster


class ProcessConsumer(WebsocketConsumer):
    def connect(self):
        self.page = self.scope["url_route"]["kwargs"]["page"]
        if not self.page:
            self.close()
            return
        self.room_group_name = f"page_{self.page}"

        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.user = self.scope["user"]
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        job_number = text_data_json["job_number"]
        print(f"consumer_job_number: {job_number}")
        action = text_data_json["action"]
        print(f"consumer_action: {action}")

        if action == "move":
            now = timezone.now()
            try:
                SerializeMaster.objects.filter(Q(job_number=job_number)).update(
                    start_operator="Jack Pashayan",
                    start_datetime=now,
                    end_operator="Jack Pashayan",
                    end_datetime=now,
                    scrapped="No",
                )
            except IntegrityError as e:
                # do something
                messages.info(f"errored at {e}")

        context = {"job_number": job_number}
        text_data = render_to_string(
            "serialize/partial/drop_job.html",
            context=context,
        )
        # self.send(text_data=text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "process.message", "message": text_data}
        )

    def process_message(self, event):
        self.send(text_data=event["message"])
