from django.urls import path

from base import views


urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('send-email', views.send_email, name="send_email")
]