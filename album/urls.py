from .import views
from django.urls import path

urlpatterns = [
    path('album/', views.add_album, name="albumm"),
    path('edit/<int:id>', views.edit_album, name="edit_album"),
    path('delete/<int:id>', views.delete_album, name="delete_album"),
]

