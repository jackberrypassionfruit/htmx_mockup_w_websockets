from django.shortcuts import render, redirect
from django.db.models import Count, Q, Max


from .models import SerializeMaster, InspectionMaster
from .models_lib.load import models_dict

pages = [
    {"name": "Serialize", "slug": "serialize", "model": SerializeMaster},
    {"name": "Inspection", "slug": "sort", "model": InspectionMaster},
    {"name": "Swimlane", "slug": "swimlane"},
]


# Create your views here.
def index(request):
    context = {"pages": pages}
    return render(request, "base/index.html", context)


def page(request, page_slug):
    return redirect(page_slug)


def get_parts(request, page_slug, job_number):
    parts_filtered_by_job = (
        models_dict[page_slug]
        .objects.filter(Q(job_number=job_number))
        .values("part_id")
    )
    return render(
        request,
        f"{page_slug}/partials/parts.html",
        context={"parts": parts_filtered_by_job},
    )


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
            context={"jobs": not_scrapped_by_job, "job_search": search},
        )


def sort(request):
    if request.method == "GET":
        search = request.GET.get("q")
        search = search if search else ""

        not_scrapped_by_job = (
            InspectionMaster.objects.filter(job_number__contains=search)
            .filter(Q(scrapped="NULL"))
            .values("job_number")
            .annotate(qty_parts=Count("part_id"), scrapped=Max("scrapped"))
        )
        if request.headers.get("HX-Trigger") == "search":
            return render(
                request,
                "sort/content/gallery.html",
                context={"jobs": not_scrapped_by_job},
            )

        return render(
            request,
            "sort/index.html",
            context={"jobs": not_scrapped_by_job, "job_search": search},
        )
