from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_index, name="home_index"),
    path("<int:pk>/", views.experience_detail, name="experience_detail"),
    path("projects/", views.project_index, name="project_index"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
]