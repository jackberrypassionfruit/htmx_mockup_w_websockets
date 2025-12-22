from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page/<slug:page_slug>", views.page, name="page"),
    path(
        "get-parts/<str:page_slug>/<str:job_number>", views.get_parts, name="get-parts"
    ),
    path("serialize", views.serialize, name="serialize"),
    path("sort", views.sort, name="sort"),
    path("swimlane", views.swimlane, name="swimlane"),
    path("patch-finish", views.patch_finish, name="patch-finish"),
]
