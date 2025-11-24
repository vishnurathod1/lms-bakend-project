from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Attendance
from users.models import User
from courses.models import Course
import json
from datetime import date

@csrf_exempt
def mark_attendance(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        attendance, created = Attendance.objects.get_or_create(
            student=User.objects.get(id=data['student_id']),
            course=Course.objects.get(id=data['course_id']),
            date=data.get('date', str(date.today())),
            defaults={'status': data.get('status', 'present')}
        )
        if not created:
            attendance.status = data.get('status', 'present')
            attendance.save()
        return JsonResponse({'message': 'Attendance marked successfully', 'attendance_id': attendance.id})
    return JsonResponse({'error': 'Invalid method'}, status=400)

def get_attendance(request, student_id, course_id):
    attendances = Attendance.objects.filter(
        student_id=student_id, course_id=course_id
    ).values('date', 'status')
    return JsonResponse(list(attendances), safe=False)
