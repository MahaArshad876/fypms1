from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app_project.models import LeaveSupervisor, Supervisor, SupMessageAdmin


def supervisor_home(request):
    return render(request, "supervisor_template/home_content_sup.html")
    # return HttpResponse("Student Login Successfully")


def leave_apply_supervisor(request):
    supervisor_obj = Supervisor.objects.get(admin=request.user.id)
    leave_data = LeaveSupervisor.objects.filter(supervisor_id= supervisor_obj )
    context = {"supervisor_obj": supervisor_obj, "leave_data": leave_data}
    return render(request, "supervisor_template/leave_apply_supervisor.html", context)


def leave_apply_supervisor_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("leave_apply_supervisor"))
    else:
        leave_date = request.POST.get("leave_date")
        leave_msg = request.POST.get("leave_msg")

        supervisor_obj = Supervisor.objects.get(admin=request.user.id) #accessing current user id
        try:
            leave_obj = LeaveSupervisor(supervisor_id=supervisor_obj, leave_date=leave_date,leave_message=leave_msg, leave_status=0)
            leave_obj.save()
            messages.success(request, "Successfully Apply For Leave")
            return HttpResponseRedirect(reverse("leave_apply_supervisor"))
        except Exception as e:
            print(e)
            messages.error(request, "Apply Failed")
            return HttpResponseRedirect(reverse("leave_apply_supervisor"))


def supervisor_message(request):
    supervisor_obj = Supervisor.objects.get(admin=request.user.id)
    message_data = SupMessageAdmin.objects.filter(supervisor_id=supervisor_obj)
    context = {"supervisor_obj": supervisor_obj, "message_data": message_data}
    return render(request, "supervisor_template/supervisor_message.html", context)


def supervisor_message_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("supervisor_message"))
    else:
        message_admin = request.POST.get("supervisor_message")

        supervisor_obj = Supervisor.objects.get(admin=request.user.id)
        try:
            message_model = SupMessageAdmin(supervisor_id=supervisor_obj, message_admin=message_admin, message_reply="")
            message_model.save()
            messages.success(request, "Message Send Sucessfully")
            return HttpResponseRedirect(reverse("supervisor_message"))
        except Exception as e:
            print(e)
            messages.error(request, "Message sending Failed")
            return HttpResponseRedirect(reverse("supervisor_message"))
