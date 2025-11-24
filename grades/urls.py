from django.urls import path
from . import views

urlpatterns = [
    path('assignment/create/', views.create_assignment, name='create_assignment'),
    path('assign/', views.assign_grade, name='assign_grade'),
    path('get/<int:student_id>/', views.get_grades, name='get_grades'),
]
