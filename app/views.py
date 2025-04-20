from django.shortcuts import render, HttpResponse, redirect
from .forms import studentform, subjectForm, resultForm
from .models import student, subject, result
from django.db import connection

# Create your views here.

def home(request):
    return render(request, "home.html")

def add_student(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = studentform()
    return render(request, 'add_student.html', {'form':form})

def add_subject(request):
    if request.method == 'POST':
        form = subjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = subjectForm()
    return render(request, 'add_subject.html', {'form':form})

def add_result(request):
    if request.method == 'POST':
        form = resultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = resultForm()
    return render(request, 'add_result.html', {'form':form})

def view_topper(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_topper();")
        topper = cursor.fetchone()
    return render(request,'view_topper.html', {'topper':topper})

def view_results(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_student_result();")
        result = cursor.fetchall()

    students = []  # Renamed from 'student' to 'students'
    for row in result:
        student_id, student_name, subject_name, marks = row
        students.append({
            'student_id': student_id,
            'student_name': student_name,
            'subject_name': subject_name,
            'marks': marks,
        })
    
    return render(request, 'view_results.html', {'students': students})  # Changed from 'student' to 'students'

