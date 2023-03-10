from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('about', views.about),
    path('project', views.project),
    path('testimonial', views.testimonial),
    path('contact', views.contact),
    path('show', views.show),
]