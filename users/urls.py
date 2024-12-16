from django.urls import path

from users import views

urlpatterns = [
    path("list/", views.list),
    path("detail/<int:id>", views.detail)
]