from django.urls import path
from . import views

urlpatterns = [
    path("generate-letter/", views.generate_letter, name="generate_letter"),
]
