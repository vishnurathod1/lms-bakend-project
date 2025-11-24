from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
import json
import os

def home(request):
    # Serve the static login.html file as the first page
    login_path = os.path.join(os.path.dirname(__file__), '..', 'login.html')
    with open(login_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return HttpResponse(content, content_type='text/html')

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return JsonResponse({'success': True, 'role': user.role})
        return JsonResponse({'success': False, 'error': 'Invalid credentials'})
    # Serve the static login.html file
    login_path = os.path.join(os.path.dirname(__file__), '..', 'login.html')
    with open(login_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return HttpResponse(content, content_type='text/html')

def serve_static(request, path):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        content_type = 'text/plain'
        if path.endswith('.css'):
            content_type = 'text/css'
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        elif path.endswith('.js'):
            content_type = 'application/javascript'
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        elif path.endswith('.html'):
            content_type = 'text/html'
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        elif path.endswith('.png'):
            content_type = 'image/png'
            with open(file_path, 'rb') as f:
                content = f.read()
        elif path.endswith('.jpg') or path.endswith('.jpeg'):
            content_type = 'image/jpeg'
            with open(file_path, 'rb') as f:
                content = f.read()
        else:
            with open(file_path, 'rb') as f:
                content = f.read()
        return HttpResponse(content, content_type=content_type)
    return HttpResponseNotFound()
