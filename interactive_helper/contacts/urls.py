from django.urls import path, include
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('edit_contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('upcoming_birthdays_list/', views.upcoming_birthdays_list, name='upcoming_birthdays_list'),
]