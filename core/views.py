from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.contrib import messages

from .models import SerializeMaster
from django.db.models import Count, Q, Max

from django.utils import timezone

# Create your views here.


# Create your views here.
def index(request):
    pages = [
        {"name": "Serialize", "slug": "serialize"},
        {"name": "Swimlane", "slug": "schedule"},
    ]
    context = {"pages": pages}
    return render(request, "base/index.html", context)


def page(request, page_slug):
    context = {
        "pages": [
            {"name": "Serialize", "slug": "serialize"},
            {"name": "Swimlane", "slug": "swimlane"},
        ]
    }
    if page_slug == "serialize":
        return redirect("serialize")

    return render(request, f"{page_slug}/index.html", context)


def serialize(request):
    if request.method == "GET":
        search = request.GET.get("q")
        search = search if search else ""

        not_scrapped_by_job = (
            SerializeMaster.objects.filter(job_number__contains=search)
            .filter(Q(scrapped="NULL"))
            .values("job_number")
            .annotate(qty_parts=Count("part_id"), scrapped=Max("scrapped"))
        )
        if request.headers.get("HX-Trigger") == "search":
            return render(
                request,
                "serialize/content/gallery.html",
                context={"jobs": not_scrapped_by_job},
            )

        return render(
            request,
            "serialize/index.html",
            # "testing/modal.html",
            context={"jobs": not_scrapped_by_job, "job_search": search},
        )


def get_parts(request, job_number):
    parts_filtered_by_job = SerializeMaster.objects.filter(
        Q(job_number=job_number)
    ).values("part_id")
    return render(
        request,
        "serialize/partial/parts.html",
        context={"parts": parts_filtered_by_job},
    )


def modal_popup(request):
    context = dict(request.GET)
    context = {key: val[0] for key, val in context.items()}
    print(f"{context=}")

    return render(
        request,
        "serialize/partial/modal_confirm.html",
        context=context,
    )


def move_job(request):
    context = dict(request.POST)
    context = {key: val[0] for key, val in context.items()}
    # print(f"{context=}")
    selected_job = context["selected_job"]

    now = timezone.now()

    try:
        SerializeMaster.objects.filter(Q(job_number=selected_job)).update(
            start_operator="Jack Pashayan",
            start_datetime=now,
            end_operator="Jack Pashayan",
            end_datetime=now,
            scrapped="No",
        )
    except IntegrityError as e:
        # do something
        messages.info(request, f"errored at {e}")

    not_scrapped_by_job = (
        SerializeMaster.objects.filter(  # .filter(job_number__contains=selected_job)
            Q(scrapped="NULL")
        )
        .values("job_number")
        .annotate(qty_parts=Count("part_id"), scrapped=Max("scrapped"))
    )
    print(f"{not_scrapped_by_job=}")
    if request.headers.get("HX-Trigger") == "move":
        return render(
            request,
            "serialize/content/gallery.html",
            context={"jobs": not_scrapped_by_job},
        )


# this works, which is sick
# though all it really does is remove the <div>'s children, which is not the same as removing it
def drop_job(request, job_number):
    context = {"job_number": job_number}
    return render(
        request,
        "serialize/partial/drop_job.html",
        context=context,
    )
