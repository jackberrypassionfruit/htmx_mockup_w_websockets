from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page/<slug:page_slug>", views.page, name="page"),
    path("serialize", views.serialize, name="serialize"),
    path("serialize/get-parts/<str:job_number>", views.get_parts, name="get-parts"),
    path("serialize/move-job/", views.move_job, name="move-job"),
    path("serialize/drop-job/<str:job_number>", views.drop_job, name="drop-job"),
]
