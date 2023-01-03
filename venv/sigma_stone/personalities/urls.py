from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('sigma_register', views.register, name="register"),
    path("list/delete/<int:id>", views.delete, name='delete'),
]