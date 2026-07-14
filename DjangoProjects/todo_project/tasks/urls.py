from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pdf/<str:person_id>/", views.generate_pdf, name="generate_pdf"),
]