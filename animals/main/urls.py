from django.urls import path
from .views import animal, family

urlpatterns = [
    path('animal/<int:num>', animal),
    path('family/<int:num>', family),
]
