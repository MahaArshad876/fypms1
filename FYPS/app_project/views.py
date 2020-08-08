from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from app_project.EmailBackend import EmailBackEnd


def Home(request):
    return render(request, "index.html")


def loginUser(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h3>Method Not Allowed")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
            # return HttpResponse("Username: " + request.POST.get("email")+" Password: " + request.POST.get("password"))
                return HttpResponseRedirect("/admin_home")
            elif user.user_type == "2":
                return HttpResponseRedirect("/supervisor_home")
            else:
                return HttpResponseRedirect("/student_home")
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/login")


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User: " + request.user.email + " User_Type: " + str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login")

