from django.http import HttpResponse
from django.shortcuts import render


def student_home(request):
    return render(request, "student_template/home_content_stud.html")
    # return HttpResponse("Student Login Successfully")
