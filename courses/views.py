from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Course, Enrollment
from users.models import User
import json

@csrf_exempt
def create_course(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        course = Course.objects.create(
            title=data['title'],
            description=data['description'],
            trainer=User.objects.get(id=data['trainer_id'])
        )
        return JsonResponse({'message': 'Course created successfully', 'course_id': course.id})
    return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt
def enroll_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        enrollment = Enrollment.objects.create(
            student=User.objects.get(id=data['student_id']),
            course=Course.objects.get(id=data['course_id'])
        )
        return JsonResponse({'message': 'Student enrolled successfully', 'enrollment_id': enrollment.id})
    return JsonResponse({'error': 'Invalid method'}, status=400)

def get_courses(request):
    courses = Course.objects.all().values('id', 'title', 'description', 'trainer__username')
    return JsonResponse(list(courses), safe=False)
