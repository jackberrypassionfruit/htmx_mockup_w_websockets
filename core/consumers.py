import json

from django.template.loader import render_to_string
from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync

from .models_lib.load import sp_MoveSerializeTransact

class ProcessConsumer(WebsocketConsumer):
    def connect(self):
        # self.page = self.scope["url_route"]["kwargs"]["page"]
        # if not self.page:
        #     self.close()
        #     return
        self.room_group_name = "cores_hub"
        # comment out because I want each page to affect each other
        # self.room_group_name = f"page_{self.page}"

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
        page = text_data_json["page"]
        action = text_data_json["action"]
        
        eng_toggle = text_data_json["eng_toggle"] == 'on'
        mrb_toggle = text_data_json["mrb_toggle"] == 'on'
        css_toggle = text_data_json["css_toggle"] == 'on'
        
        # print('text_data_json:')
        # print(text_data_json)

        if action == "move":
            # update_end_job(
            #     model=models_dict[self.page],
            #     job_number=job_number,
            #     user_name="Jack Pashayan",
            # )
            if page == 'serialize':
                sp_MoveSerializeTransact(
                    job_number=job_number,
                    page=page,
                    sub_process='',
                    eng_toggle=eng_toggle,
                    mrb_toggle=mrb_toggle,
                    css_toggle=css_toggle,
                    current_user="Jack Pashayan",
                )

            print("sort new job: ", job_number)
            new_row = {
                "job_number": job_number,
                "request_type": "Production",
                "qty_parts": 24,
            }
            context = {"row": new_row}

            # Create a fake routing for testing
            slug_mapping = {
                "serialize": "sort",
                "sort": "patch-finish",
                "patch-finish": "serialize",
            }
            text_data = render_to_string(
                f"{slug_mapping[page]}/partials/add-job.html",
                context=context,
            )
            # self.send(text_data=text_data)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {"type": "process.message", "message": text_data}
            )

        # remove the row from the current page
        context = {"job_number": job_number}
        text_data = render_to_string(
            f"{page}/partials/drop-job.html",
            # f"{self.page}/partials/drop-job.html",
            context=context,
        )
        # self.send(text_data=text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "process.message", "message": text_data}
        )

    def process_message(self, event):
        self.send(text_data=event["message"])
