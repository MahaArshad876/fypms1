from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from app_project.models import CustomUser, Supervisor, Students


def admin_home(request):
    return render(request, "admin_template/home_content.html")


def add_supervisor(request):
    return render(request, "admin_template/add_supervisor.html")


def add_supervisor_save(request):
    if request.method != "POST":
        return HttpResponse("Method is Not POST")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
#         now creating customuser object by method .creae_user()
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=first_name, last_name=last_name, user_type=2)
            user.supervisor.address = address
            user.save()
            messages.success(request, "Add Supervisor Successfully")
            return HttpResponseRedirect(request, "/add_supervisor")
            # return  HttpResponse("Supervisor Added")
        except Exception as e:
            print(e)
            messages.error(request, "Failed")
            return HttpResponseRedirect("/add_supervisor")
            return HttpResponse("Failed")


def add_student(request):
    return render(request, "admin_template/add_student.html")


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method is Not Post")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        #         now creating customuser object by method .creae_user()
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=first_name, last_name=last_name, user_type=3)
            user.students.address = address
            user.students.gender = gender
            user.students.session_start_at = session_start
            user.students.session_end_at = session_end
            user.save()
            messages.success(request, "Add Student Successfully")
            return HttpResponseRedirect(request, "/add_student")
            # return  HttpResponse("Student Added")
        except Exception as e:
            print(e)
            messages.error(request, "Failed")
            return HttpResponseRedirect("/add_student")
            # return HttpResponse("Failed")


def manage_supervisor(request):
    supervisors = Supervisor.objects.all()
    context = {"supervisors": supervisors}
    return render(request, "admin_template/manage_supervisor.html", context)


def manage_student(request):
    students = Students.objects.all()
    context = {"students": students}
    return render(request, "admin_template/manage_student.html", context)


def edit_supervisor(request, supervisor_id):
    # return HttpResponse("Supervisor id:" +zeeshan_id )
    supervisors = Supervisor.objects.get(admin=supervisor_id)
    context = {"supervisors": supervisors}
    return render(request, "admin_template/edit_supervisor.html", context)


def edit_supervisor_save(request):
    if request.method != "POST":
        return HttpResponse("Method is Not Valid")
    else:
        supervisor_id = request.POST.get("supervisors_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.get(id=supervisor_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            supervisor_model = Supervisor.objects.get(admin=supervisor_id)
            supervisor_model.address = address
            supervisor_model.save()

            messages.success(request, "Supervisor Edited Successfully")
            return HttpResponseRedirect("/edit_supervisor/"+supervisor_id)
        except Exception as e:
            print(e)
            messages.error(request, "Editing Failed")
            return HttpResponseRedirect("/edit_supervisor/"+supervisor_id)


def edit_student(request, stud_id):
    student = Students.objects.get(admin=stud_id)
    context = {"student": student}
    return render(request, "admin_template/edit_student.html", context)


def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Allowed")
    else:
        stud_id = request.POST.get("stud_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        session_start_at = request.POST.get("session_start")
        session_end_at = request.POST.get("session_end")
        try:
            user = CustomUser.objects.get(id = stud_id)
            # user = CustomUser.objects.get(id=stud_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            stud_model = Students.objects.get(admin=stud_id)
            stud_model.address = address
            stud_model.gender = gender
            stud_model.session_start_at = session_start_at
            stud_model.session_end_at = session_end_at
            stud_model.save()

            messages.success(request, "Student Edited Successfully")
            return HttpResponseRedirect("/edit_student/"+stud_id)
        except Exception as e:
            print(e)
            messages.error(request, "Editing Failed")
            return HttpResponseRedirect("/edit_student/"+stud_id)