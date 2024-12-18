from django.urls import path

from users import views

urlpatterns = [
    path('list/', views.list, name='user_list'),
    path('detail/<int:id>/', views.detail, name='details'),
    path('delete/<int:id>/', views.delete, name='delete'),
]