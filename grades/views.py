from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Assignment, Grade
from users.models import User
from courses.models import Course
import json

@csrf_exempt
def create_assignment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        assignment = Assignment.objects.create(
            title=data['title'],
            description=data['description'],
            course=Course.objects.get(id=data['course_id']),
            trainer=User.objects.get(id=data['trainer_id']),
            due_date=data['due_date']
        )
        return JsonResponse({'message': 'Assignment created successfully', 'assignment_id': assignment.id})
    return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt
def assign_grade(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        grade, created = Grade.objects.get_or_create(
            student=User.objects.get(id=data['student_id']),
            assignment=Assignment.objects.get(id=data['assignment_id']),
            defaults={
                'score': data['score'],
                'max_score': data.get('max_score', 100),
                'feedback': data.get('feedback', '')
            }
        )
        if not created:
            grade.score = data['score']
            grade.max_score = data.get('max_score', 100)
            grade.feedback = data.get('feedback', '')
            grade.save()
        return JsonResponse({'message': 'Grade assigned successfully', 'grade_id': grade.id})
    return JsonResponse({'error': 'Invalid method'}, status=400)

def get_grades(request, student_id):
    grades = Grade.objects.filter(student_id=student_id).values(
        'assignment__title', 'score', 'max_score', 'feedback', 'graded_at'
    )
    return JsonResponse(list(grades), safe=False)
