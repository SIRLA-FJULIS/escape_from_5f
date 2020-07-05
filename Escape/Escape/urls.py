
from django.contrib import admin
from django.urls import path
from Escape_story.views import Beginning,Five_A,Toilet,Corridor_I,Corridor_II,Department_office
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Beginning),
    path('NUE=/',Five_A), #NUE=
    path('Y29ycmlkb3JfaQ==/',Corridor_I), #Y29ycmlkb3JfaQ==
    path('Y29ycmlkb3JfaWk=/',Corridor_II), #Y29ycmlkb3JfaWk=
    path('ZGVwYXJ0bWVudF9vZmZpY2U=/',Department_office), #ZGVwYXJ0bWVudF9vZmZpY2U=
    path('dG9pbGV0/',Toilet), #dG9pbGV0
]