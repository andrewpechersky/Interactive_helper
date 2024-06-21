from django.contrib import admin
from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
]