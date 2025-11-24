from django.urls import path
from . import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('get/<int:student_id>/<int:course_id>/', views.get_attendance, name='get_attendance'),
]
