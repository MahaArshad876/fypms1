
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app_project.forms import AddStudentForm, EditStudentForm
from app_project.models import CustomUser, Supervisor, Students, Programs, Sections, StudMessageAdmin, \
    ApplyProjectApproval, LeaveSupervisor, SupMessageAdmin


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
            return HttpResponseRedirect(reverse("add_supervisor"))
            # return  HttpResponse("Supervisor Added")
        except Exception as e:
            print(e)
            messages.error(request, "Failed")
            return HttpResponseRedirect(reverse("add_supervisor"))
            return HttpResponse("Failed")


def add_program(request):
    return render(request, "admin_template/add_program.html")


def add_program_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Post")
    else:
        program = request.POST.get("program")
        try:
            program_model = Programs(program_name=program)
            program_model.save()
            messages.success(request, "Add Program Successfully")
            return HttpResponseRedirect(reverse("add_program"))
        except:
            messages.error(request, "Failed")
            return HttpResponseRedirect(reverse("add_program"))
            # return HttpResponse("Failed")


def manage_program(request):
    programs = Programs.objects.all()
    context = {"programs": programs}
    return render(request, "admin_template/manage_program.html", context)


def edit_program(request, program_id):
    programs = Programs.objects.get(id=program_id)
    context = {"programs": programs}
    return render(request, "admin_template/edit_program.html", context)


def edit_program_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        program_id = request.POST.get("program_id")
        program_name = request.POST.get("program")

        try:
            program = Programs.objects.get(id=program_id)
            program.program_name = program_name
            program.save()
            messages.success(request, "Successfully Edited Course")
            return HttpResponseRedirect(reverse("edit_program", kwargs={"program_id":program_id}))
        except:
            messages.error(request, "Failed to Edit Course")
            return HttpResponseRedirect(reverse("edit_program",kwargs={"program_id":program_id}))


def edit_assign_sup(request, section_id):
    section = Sections.objects.get(id=section_id)
    programs = Programs.objects.all()
    supervisors = CustomUser.objects.filter(user_type=2)
    context = {"section": section,"programs": programs, "supervisors": supervisors}
    return render(request, "admin_template/edit_assign_sup.html", context)


def edit_assign_sup_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        section_id = request.POST.get("section_id")
        section_name = request.POST.get("section")
        supervisor_id = request.POST.get("supervisor")
        program_id = request.POST.get("program")

        try:
            section = Sections.objects.get(id=section_id)
            section.section_name = section_name
            supervisor = CustomUser.objects.get(id=supervisor_id)
            section.supervisor_id = supervisor
            program = Programs.objects.get(id=program_id)
            section.program_id = program
            section.save()
            messages.success(request, "Successfully Change Supervisor")
            return HttpResponseRedirect(reverse("edit_assign_sup",  kwargs={"section_id": section_id}))
        except:
            messages.error(request, "Failed to Change Supervisor")
            return HttpResponseRedirect(reverse("edit_assign_sup", kwargs={"section_id": section_id}))


def assign_supervisor(request):
    programs = Programs.objects.all()
    supervisors = CustomUser.objects.filter(user_type=2)
    context = {"programs": programs, "supervisors":supervisors}
    return render(request, "admin_template/assign_supervisor.html", context)


def assign_supervisor_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        section_name = request.POST.get("section")
        # course_id = request.POST.get("course")
        program_id = request.POST.get("program")
        program = Programs.objects.get(id=program_id)
        supervisor_id = request.POST.get("supervisor")
        supervisor = CustomUser.objects.get(id=supervisor_id)

        try:
            assign_sup = Sections(section_name=section_name, program_id=program, supervisor_id=supervisor)
            assign_sup.save()
            messages.success(request, "Successfully Assign Supervisor")
            return HttpResponseRedirect(reverse("assign_supervisor"))
        except:
            messages.error(request, "Failed")
            return HttpResponseRedirect(reverse("assign_supervisor"))


def change_supervisor(request):
    sections = Sections.objects.all()
    context = {"sections": sections}
    return render(request, "admin_template/change_supervisor.html", context)


def add_student(request):
    programs = Programs.objects.all()
    form = AddStudentForm()
    context = {"programs": programs, "form": form}
    return render(request, "admin_template/add_student.html", context)


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method is Not Post")
    else:
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            roll_no = form.cleaned_data["roll_no"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            gender = form.cleaned_data["gender"]
            program_id = form.cleaned_data["program"]
            section_id = form.cleaned_data["section"]
            semester = form.cleaned_data["semester"]
            session_start = form.cleaned_data["session_start"]
            session_end = form.cleaned_data["session_end"]

            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            #         now creating customuser object by method .creae_user()
            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                      first_name=first_name, last_name=last_name, user_type=3)
                user.students.roll_no = roll_no
                user.students.address = address
                user.students.gender = gender
                program_obj = Programs.objects.get(id=program_id)
                user.students.program_id = program_obj
                section_obj = Sections.objects.get(id=section_id)
                user.students.section_id = section_obj
                user.students.semester = semester
                user.students.session_start_at = session_start
                user.students.session_end_at = session_end
                user.students.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "Add Student Successfully")
                return HttpResponseRedirect(reverse("add_student"))
                # return  HttpResponse("Student Added")
            except Exception as e:
                print(e)
                messages.error(request, "Failed")
                return HttpResponseRedirect(reverse("add_student"))
                # return HttpResponse("Failed")
        else:
            form = AddStudentForm(request.POST)
            return render(request, "admin_template/add_student.html", {"form": form})



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
            return HttpResponseRedirect(reverse("edit_supervisor", kwargs={"supervisor_id": supervisor_id}))
        except Exception as e:
            print(e)
            messages.error(request, "Editing Failed")
            return HttpResponseRedirect(reverse("edit_supervisor", kwargs={"supervisor_id": supervisor_id}))


def edit_student(request, stud_id):
    request.session['stud_id'] = stud_id
    student = Students.objects.get(admin=stud_id)
    form = EditStudentForm()
    try:
        form.fields["email"].initial=student.admin.email
        form.fields["roll_no"].initial=student.roll_no
        form.fields["first_name"].initial=student.admin.first_name
        form.fields["last_name"].initial=student.admin.last_name
        form.fields["username"].initial=student.admin.username
        form.fields["address"].initial=student.address
        form.fields["program"].initial=student.program_id.id
        form.fields["section"].initial=student.section_id.id
        form.fields["semester"].initial=student.semester
        form.fields["gender"].initial=student.gender
        form.fields["session_start"].initial=student.session_start_at
        form.fields["session_end"].initial=student.session_end_at
    except Exception as e:
        print(e)
    context = {"form": form, "id": stud_id, "username": student.admin.username }
    return render(request, "admin_template/edit_student.html", context)


def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Allowed")
    else:
        stud_id = request.session.get("stud_id")
        if stud_id == None:
            return HttpResponseRedirect(reverse("manage_student"))

        form = EditStudentForm(request.POST, request.FILES)
        if form.is_valid():
            roll_no = form.cleaned_data["roll_no"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            program_id = form.cleaned_data["program"]
            section_id = form.cleaned_data["section"]
            semester = form.cleaned_data["semester"]
            gender = form.cleaned_data["gender"]
            session_start_at = form.cleaned_data["session_start"]
            session_end_at = form.cleaned_data["session_end"]

            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                user = CustomUser.objects.get(id = stud_id)
                # user = CustomUser.objects.get(id=stud_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.save()

                stud_model = Students.objects.get(admin=stud_id)
                stud_model.roll_no =roll_no
                stud_model.address = address
                program = Programs.objects.get(id=program_id)
                stud_model.program_id = program
                section = Sections.objects.get(id=section_id)
                stud_model.section_id = section
                stud_model.semester = semester
                stud_model.gender = gender
                stud_model.session_start_at = session_start_at
                stud_model.session_end_at = session_end_at
                if profile_pic_url != None:
                    stud_model.profile_pic = profile_pic_url
                stud_model.save()
                del request.session['stud_id']

                messages.success(request, "Student Edited Successfully")
                return HttpResponseRedirect(reverse("edit_student", kwargs={"stud_id": stud_id}))
            except Exception as e:
                print(e)
                messages.error(request, "Editing Failed")
                return HttpResponseRedirect(reverse("edit_student", kwargs={"stud_id": stud_id}))
        else:
            form = EditStudentForm(request.POST)
            student = Students.objects.get(admin=stud_id)
            context = {"form":form,  "id": stud_id, "username": student.admin.username }
            return render(request, "admin_template/edit_student.html", context)

from django.http import JsonResponse
import  json
@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=CustomUser.objects.filter(email = email).exists()
    if user_obj:
        # return HttpResponse(True)
        msg = {'email': 'Email Not Available'}
        msgj = json.dumps(msg)
        return JsonResponse(msgj, safe= False)
    else:
        msg = {'email': 'Email is Available'}
        msgj = json.dumps(msg)
        return JsonResponse(msgj, safe= False)


@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def student_feedback_message(request):
    # student_obj = Students.objects.get(admin=stud_id)
    # message_data = StudMessageAdmin.objects.filter(student_id=student_obj)
    feedback_date = StudMessageAdmin.objects.all()
    context = {"feedback_date": feedback_date,}
    return render(request, "admin_template/student_feedback.html", context)



@csrf_exempt
def student_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=StudMessageAdmin.objects.get(id=feedback_id)
        feedback.admin_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")


def supervisor_feedback_message(request):
    feedback_date = SupMessageAdmin.objects.all()
    context = {"feedback_date": feedback_date,}
    return render(request, "admin_template/supervisor_feedback.html", context)


@csrf_exempt
def supervisor_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=SupMessageAdmin.objects.get(id=feedback_id)
        feedback.message_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")


def student_project_view(request):
    project_approvals = ApplyProjectApproval.objects.all()
    context = {"project_approvals": project_approvals}
    return render(request, "admin_template/student_project.html", context)


def supervisor_leave_view(request):
    supervisor_leaves = LeaveSupervisor.objects.all()
    context = {"supervisor_leaves": supervisor_leaves}
    return render(request, "admin_template/supervisor_leave_view.html", context)


def student_project_approve(request, project_id):
    approval = ApplyProjectApproval.objects.get(id=project_id)
    approval.approval_status = 1
    approval.save()
    return HttpResponseRedirect(reverse("student_project_view"))


def student_project_disapprove(request, project_id):
    approval = ApplyProjectApproval.objects.get(id=project_id)
    approval.approval_status = 2
    approval.save()
    return HttpResponseRedirect(reverse("student_project_view"))


def supervisor_leave_approve(request, leave_id):
    leav = LeaveSupervisor.objects.get(id=leave_id)
    leav.leave_status = 1
    leav.save()
    return HttpResponseRedirect(reverse("supervisor_leave_view"))


def supervisor_leave_disapprove(request, leave_id):
    leav = LeaveSupervisor.objects.get(id=leave_id)
    leav.leave_status = 2
    leav.save()
    return HttpResponseRedirect(reverse("supervisor_leave_view"))