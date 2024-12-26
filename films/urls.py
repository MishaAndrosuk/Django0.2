from django.urls import path

from films import views

urlpatterns = [
    path('', views.list, name='films_list'),
    path('detail/<int:id>/', views.detail, name='details'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path("create/", views.create)
]