from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('view_report/', views.view_report, name='view_report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('system_settings/', views.system_settings, name='system_settings'),
    path('user_roles/', views.user_roles, name='user_roles'),
    path('notifications/', views.notifications, name='notifications'),
    path('activity_monitoring/', views.activity_monitoring, name='activity_monitoring'),
    path('feedback/', views.feedback, name='feedback'),
    path('security_settings/', views.security_settings, name='security_settings'),
    path('performance/', views.performance, name='performance'),
    path('compliance/', views.compliance, name='compliance'),
    path('system_updates/', views.system_updates, name='system_updates'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('student_assignments/', views.student_assignments, name='student_assignments'),
    path('attendance/', views.attendance, name='attendance'),
    path('admin_data_sorting/', views.admin_data_sorting, name='admin_data_sorting'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    path('show_student/', views.show_student, name='show_student'),
    path('show_trainer/', views.show_trainer, name='show_trainer'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
]
