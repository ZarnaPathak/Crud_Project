from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_student(request):
    return render(request, 'addStudent.html')