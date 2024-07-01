from django.contrib import admin
from django.urls import path
import example
import example.urls
from example import views
urlpatterns = [
    path('',views.test)
]