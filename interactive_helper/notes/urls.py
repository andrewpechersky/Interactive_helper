from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.main, name='index'),
    path('add_notes/', views.note, name='add_notes'),
    path('tag/', views.tag, name='tag'),
    path('detail/<int:note_id>', views.detail, name='detail'),
    path('done/<int:note_id>', views.set_done, name='set_done'),
    path('edit_note/<int:pk>/', views.edit_note, name='edit'),
    path('delete/<int:note_id>', views.delete_note, name='delete'),
    path('tag/<int:tag_id>/delete/', views.delete_tag, name='delete_tag'),
]