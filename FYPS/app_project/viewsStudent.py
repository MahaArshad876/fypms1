from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app_project.models import Students, ApplyProjectApproval, StudMessageAdmin


def student_home(request):
    return render(request, "student_template/home_content_stud.html")
    # return HttpResponse("Student Login Successfully")


def apply_project_approval(request):
    student_obj = Students.objects.get(admin=request.user.id)
    approval_data = ApplyProjectApproval.objects.filter(student_id=student_obj)
    context = {"student_obj": student_obj, "approval_data": approval_data}
    return render(request, "student_template/apply_project_approval.html", context)


def apply_project_approval_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("apply_project_approval"))
    else:
        apply_date = request.POST.get("apply_date")
        project_title = request.POST.get("project_title")
        abstract = request.POST.get("abstract")
        conclusion = request.POST.get("conclusion")

        student_obj = Students.objects.get(admin=request.user.id)  # accessing current user id
        try:
            approval_obj = ApplyProjectApproval(student_id=student_obj, apply_date=apply_date, project_title=project_title,
                                                abstract=abstract, conclusion=conclusion, approval_status=0)
            approval_obj.save()
            messages.success(request, "Apply Successfully")
            return HttpResponseRedirect(reverse("apply_project_approval"))
        except Exception as e:
            print(e)
            messages.error(request, "Apply Failed")
            return HttpResponseRedirect(reverse("apply_project_approval"))


def student_message_admin(request):
    student_obj = Students.objects.get(admin=request.user.id)
    message_data = StudMessageAdmin.objects.filter(student_id=student_obj)
    context = {"student_obj": student_obj, "message_data": message_data}
    return render(request, "student_template/student_message_admin.html", context)


def student_message_admin_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("student_message_admin"))
    else:
        student_message = request.POST.get("student_message")

        student_obj = Students.objects.get(admin=request.user.id)
        try:
            message_model = StudMessageAdmin(student_id=student_obj, student_message=student_message, admin_reply="")
            message_model.save()
            messages.success(request, "Message Send Sucessfully")
            return HttpResponseRedirect(reverse("student_message_admin"))
        except Exception as e:
            print(e)
            messages.error(request, "Message sending Failed")
            return HttpResponseRedirect(reverse("student_message_admin"))