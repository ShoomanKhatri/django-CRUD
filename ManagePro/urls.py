from django.urls import path
from .views import student_list_create, student_update_delete

urlpatterns = [
    path('students/', student_list_create),
    path('students/<int:pk>/', student_update_delete),
]
