from django.urls import path

from films import views

urlpatterns = [
    path('', views.list, name='list_films'),
    path('detail/<int:id>/', views.detail, name='film_details'),
    path('delete/<int:id>/', views.delete, name='delete_film'),
    path('edit/<int:id>/', views.edit, name='edit_film'),
    path("create/", views.create),
    path('film/save/<int:id>/', views.save_film, name='save_film'),
    path('saved/', views.saved, name='saved_films'),
]