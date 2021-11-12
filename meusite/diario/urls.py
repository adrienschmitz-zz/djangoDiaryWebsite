from django.urls import path
from . import views

urlpatterns = [
    path('', views.day_list, name='day_list'),
    path("update_server/", views.update, name="update"),
    path('day/<int:pk>/', views.day_detail, name='day_detail'),
]
