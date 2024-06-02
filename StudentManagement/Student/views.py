from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def home(request):
    std = Student.objects.all()
    return render(request, 'home.html', {'std': std})

def add_student(request):
    if request.method == "POST":
        print("Added")
        # fetching Student Inputs
        stds_roll = request.POST.get("std_roll")        
        stds_name = request.POST.get("std_name")        
        stds_email = request.POST.get("std_email")        
        stds_address = request.POST.get("std_address")        
        stds_phone = request.POST.get("std_phone")   

        #creating object for Student model and adding fetched inputs into table
        std = Student()
        std.roll = stds_roll
        std.name = stds_name
        std.email = stds_email
        std.address = stds_address
        std.phone = stds_phone

        # save object to add info in table
        std.save()
        return redirect("/student/home")

    return render(request, 'addStudent.html')

def delete_student(request, roll):
    std = Student.objects.get(pk=roll)
    std.delete()
    return redirect("/student/home")