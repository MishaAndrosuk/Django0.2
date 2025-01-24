from django.urls import path

from liked import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clear/", views.clear, name="clear"),
    path("add/<int:id>", views.add, name="add"),
    path("add/<int:id>/<int:quantity>", views.add, name="add_with_quantity"),
    path("liked/delete/<int:id>", views.delete_liked, name='delete_from_liked'),
]
