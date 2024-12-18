from django.urls import path

from users import views

urlpatterns = [
    path("list/", views.list, name="users_list"),
    path("detail/<int:id>/", views.detail, name="user_details"),
]