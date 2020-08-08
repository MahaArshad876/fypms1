from django.http import HttpResponse
from django.shortcuts import render


def supervisor_home(request):
    return render(request, "supervisor_template/home_content_sup.html")
    # return HttpResponse("Student Login Successfully")