from django.http import request
from django.shortcuts import render, redirect

# Create your views here.


def CGPA(request):
    if request.method == "POST":
        number_of_courses = request.POST["Number of Courses"]
        gpa = request.POST["GPA"]
        print(gpa)
        return redirect("/")

    return render(request, "cgpa.html")
