from django.urls import path

from users import views

urlpatterns = [
    path('', views.list, name='list_users'),
    path('detail/<int:id>/', views.detail, name='user_details'),
    path('delete/<int:id>/', views.delete, name='delete_user'),
    path('edit/<int:id>/', views.edit, name='edit_user'),
    path("create/", views.create)
]