#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home),
    path('project/',views.project,name='project'),
    path('count/',views.count, name='count'),
    path('about/',views.about, name='about'),
]
