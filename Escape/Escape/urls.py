
from django.contrib import admin
from django.urls import path
from Escape_story.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
]
