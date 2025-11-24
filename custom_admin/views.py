from django.shortcuts import render

def admin_home(request):
    return render(request, 'admin_home.html')


def manage_users(request):
    return render(request, 'admin/manage_users.html')

def view_report(request):
    return render(request, 'admin/view_report.html')

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def system_settings(request):
    return render(request, 'admin/system_settings.html')

def user_roles(request):
    return render(request, 'admin/user_roles.html')

def notifications(request):
    return render(request, 'admin/notifications.html')

def activity_monitoring(request):
    return render(request, 'admin/activity_monitoring.html')

def feedback(request):
    return render(request, 'admin/feedback.html')

def security_settings(request):
    return render(request, 'admin/security_settings.html')

def performance(request):
    return render(request, 'admin/performance_metrics.html')

def compliance(request):
    return render(request, 'admin/admin_complaints.html')

def system_updates(request):
    return render(request, 'admin/system_updates.html')

def contact(request):
    return render(request, 'admin/contact.html')

def about(request):
    return render(request, 'admin/about.html')

def student_assignments(request):
    return render(request, 'admin/student_assignments.html')

def attendance(request):
    return render(request, 'admin/attendance.html')

def admin_data_sorting(request):
    return render(request, 'admin/admin_data_sorting.html')

def add_trainer(request):
    return render(request, 'admin/add_trainer.html')

def show_student(request):
    return render(request, 'admin/show_student.html')

def show_trainer(request):
    return render(request, 'admin/show_trainer.html')

def admin_profile(request):
    return render(request, 'admin/admin_profile.html')
