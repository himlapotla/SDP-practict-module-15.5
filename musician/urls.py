from .import views
from django.urls import path

urlpatterns = [
    path('musician/', views.add_musician, name="musician"),
    path('editt/<int:id>', views.editt_musician, name="editt_musician"),
]


