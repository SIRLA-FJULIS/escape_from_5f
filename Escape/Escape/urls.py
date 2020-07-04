
from django.contrib import admin
from django.urls import path
from Escape_story.views import Beginning,Five_A,Toilet,Corridor_I,Corridor_II,Department_office

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Beginning),
    path('5A/',Five_A),
    path('corridor_i/',Corridor_I),
    path('corridor_ii/',Corridor_II),
    path('department_office/',Department_office),
    path('toilet/',Toilet),
]