from django.shortcuts import render, redirect
from django.db.models import Count, Q, Max

from .models import (
    SerializeMaster,
    InspectionMaster,
    PatchMaster,
    CoresMasterDetails,
    CoresMasterChangelog,
)
from .dcap_models import (
    Cores2SerializeMaster,
    Cores2InspectionMaster,
    Cores2PatchMaster,
    Cores2MasterDetails,
    Cores2MasterChangelog,
)
from .models_lib.load import models_dict
from .models_lib.service_class import test_call_sproc, test_get_view, test_get_serial_parts

from .libs.swimlane.extract import get_scheduled_prints_df, get_active_printers_df
from .libs.swimlane.transform import (
    partition_prints_by_printer_ordered_w_style,
    filter_and_cache_prints,
    schedule_cached_prints,
)

pages = [
    {"name": "Serialize", "slug": "serialize"},
    {"name": "Inspection", "slug": "sort"},
    {
        "name": "Patch",
        "subpages": [
            {
                "name": "Patch & Finish",
                "slug": "patch-finish",
            },
            {
                "name": "Cure",
                "slug": "patch-cure",
            },
            {
                "name": "Sand",
                "slug": "patch-sand",
            },
        ],
    },
    {"name": "Swimlane", "slug": "swimlane"},
]


# Create your views here.
def index(request):
    context = {"pages": pages}
    return render(request, "base/index.html", context)


def page(request, page_slug):
    return redirect(page_slug)


def get_parts(request, page_slug, job_number):
    if str.startswith(page_slug, "patch"):
        parts_filtered_by_job = PatchMaster.objects.filter(
            Q(master_fk_id__job_number=job_number)
        ).values("master_fk_id__part_id")
    elif page_slug == 'serialize':
        parts_filtered_by_job = test_get_serial_parts(job_number)
    else:
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
        
        not_scrapped_by_job = test_get_view(search)
        
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
            Cores2InspectionMaster.objects.filter(job_number__contains=search)
            .filter(scrapped__isnull=True)
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


def patch_finish(request):
    if request.method == "GET":
        search = request.GET.get("q")
        search = search if search else ""

        not_scrapped_by_job = (
            Cores2PatchMaster.objects.filter(master_fk_id__job_number__icontains=search)
            .filter(Q(scrapped="NULL") & Q(sub_process="Patch & Finish"))
            .values("master_fk_id__job_number")
            .annotate(
                qty_parts=Count("master_fk_id__part_id"), scrapped=Max("scrapped")
            )
        )
        if request.headers.get("HX-Trigger") == "patch-finish-search":
            return render(
                request,
                "patch-finish/content/job-gallery.html",
                context={"jobs": not_scrapped_by_job},
            )

        return render(
            request,
            "patch-finish/index.html",
            context={"jobs": not_scrapped_by_job, "job_search": search},
        )


def swimlane(request):
    return render(
        request,
        "swimlane/index.html",
        context={},
    )

def test_sproc(request):
    if request.method == "POST":
        job_number = request.POST.get("job_number")
        
        test_call_sproc(job_number)
            
        return render(
            request,
            "base/partials/test-sproc-confirm.html",
            context={'job_number': job_number }
        )
        
        