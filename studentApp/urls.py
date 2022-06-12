from studentApp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("contact", views.contact),
    path("login", views.login),
    path("register", views.register),
    path("register-owner", views.register_owner),
    path("coming-soon", views.coming_soon),
    path("category/mess", views.mess),
    path("category/pg", views.pg),
    path("about-us", views.about),
    path("404", views.error_404),
    path("category/pg/nayanika-pg", views.viewdetails),
]
