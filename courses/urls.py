from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_course, name='create_course'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('list/', views.get_courses, name='get_courses'),
]
