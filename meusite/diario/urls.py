from django.urls import path
from . import views
from updater import views

urlpatterns = [
    path('', views.day_list, name='day_list'),
    path("update_server/", views.update, name="update"),
]
