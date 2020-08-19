from django.urls import path

from app_project import views, viewsAdmin, viewsStudent, viewsSupervisor

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('admin_home', viewsAdmin.admin_home, name='admin_home'),
    path('add_supervisor', viewsAdmin.add_supervisor, name="add_supervisor"),
    path('add_supervisor_save', viewsAdmin.add_supervisor_save, name="add_supervisor_save"),
    path('add_program', viewsAdmin.add_program, name="add_program"),
    path('add_program_save', viewsAdmin.add_program_save, name="add_program_save"),
    path('add_student', viewsAdmin.add_student, name="add_student"),
    path('add_student_save', viewsAdmin.add_student_save, name="add_student_save"),
    path('assign_supervisor', viewsAdmin.assign_supervisor, name="assign_supervisor"),
    path('assign_supervisor_save', viewsAdmin.assign_supervisor_save, name="assign_supervisor_save"),
    path('manage_supervisor', viewsAdmin.manage_supervisor, name="manage_supervisor"),
    path('edit_supervisor/<str:supervisor_id>/', viewsAdmin.edit_supervisor),
    path('edit_supervisor_save', viewsAdmin.edit_supervisor_save, name="edit_supervisor_save"),
    path('manage_student', viewsAdmin.manage_student, name="manage_student"),
    path('edit_student/<str:stud_id>/', viewsAdmin.edit_student, name="edit_student"),
    path('edit_student_save', viewsAdmin.edit_student_save, name="edit_student_save"),
    path('manage_program', viewsAdmin.manage_program, name="manage_program"),
    path('change_supervisor', viewsAdmin.change_supervisor, name="change_supervisor"),

    path('edit_program/<str:program_id>/', viewsAdmin.edit_program, name="edit_program"),
    path('edit_program_save', viewsAdmin.edit_program_save, name="edit_program_save"),
    path('edit_assign_sup/<str:section_id>/', viewsAdmin.edit_assign_sup, name="edit_assign_sup"),
    path('edit_assign_sup_save', viewsAdmin.edit_assign_sup_save, name="edit_assign_sup_save"),

    path('check_email_exist', viewsAdmin.check_email_exist, name="check_email_exist"),
    path('check_username_exist', viewsAdmin.check_username_exist, name="check_username_exist"),

    path('student_feedback_message', viewsAdmin.student_feedback_message, name="student_feedback_message"),
    # path('student_feedback_message_save/<str:stud_id>', viewsAdmin.student_feedback_message_save, name="student_feedback_message_save"),
    path('student_feedback_message_replied', viewsAdmin.student_feedback_message_replied, name="student_feedback_message_replied"),
    path('supervisor_feedback_message', viewsAdmin.supervisor_feedback_message, name="supervisor_feedback_message"),
    path('supervisor_feedback_message_replied', viewsAdmin.supervisor_feedback_message_replied, name="supervisor_feedback_message_replied"),

    path('student_project_view', viewsAdmin.student_project_view, name="student_project_view"),
    path('supervisor_leave_view', viewsAdmin.supervisor_leave_view, name="supervisor_leave_view"),
    path('student_project_approve/<str:project_id>', viewsAdmin.student_project_approve, name="student_project_approve"),
    path('student_project_disapprove/<str:project_id>', viewsAdmin.student_project_disapprove, name="student_project_disapprove"),
    path('supervisor_leave_approve/<str:leave_id>', viewsAdmin.supervisor_leave_approve, name="supervisor_leave_approve"),
    path('supervisor_leave_disapprove/<str:leave_id>', viewsAdmin.supervisor_leave_disapprove, name="supervisor_leave_disapprove"),



    # path('signup/', views.signup, name="signup"),

    path('student_home', viewsStudent.student_home, name="student_home"),
    path('apply_project_approval', viewsStudent.apply_project_approval, name="apply_project_approval"),
    path('apply_project_approval_save', viewsStudent.apply_project_approval_save, name="apply_project_approval_save"),
    path('student_message_admin', viewsStudent.student_message_admin, name="student_message_admin"),
    path('student_message_admin_save', viewsStudent.student_message_admin_save, name="student_message_admin_save"),

    # Supervisor Urls
    path('supervisor_home', viewsSupervisor.supervisor_home, name="supervisor_home"),
    path('leave_apply_supervisor', viewsSupervisor.leave_apply_supervisor, name="leave_apply_supervisor"),
    path('leave_apply_supervisor_save', viewsSupervisor.leave_apply_supervisor_save, name="leave_apply_supervisor_save"),
    path('supervisor_message', viewsSupervisor.supervisor_message, name="supervisor_message"),
    path('supervisor_message_save', viewsSupervisor.supervisor_message_save, name="supervisor_message_save"),


]