from django.urls import path

from app_project import views, viewsAdmin, viewsStudent, viewsSupervisor

urlpatterns = [
    path('', views.Home, name="home"),
    path('login/', views.loginUser, name="login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user),
    path('doLogin', views.doLogin, name="doLogin"),
    path('admin_home', viewsAdmin.admin_home, name='admin_home'),
    path('add_supervisor', viewsAdmin.add_supervisor, name="add_supervisor"),
    path('add_supervisor_save', viewsAdmin.add_supervisor_save, name="add_supervisor_save"),
    path('add_student', viewsAdmin.add_student, name="add_student"),
    path('add_student_save', viewsAdmin.add_student_save, name="add_student_save"),
    path('manage_supervisor', viewsAdmin.manage_supervisor, name="manage_supervisor"),
    path('edit_supervisor/<str:supervisor_id>/', viewsAdmin.edit_supervisor),
    path('edit_supervisor_save', viewsAdmin.edit_supervisor_save, name="edit_supervisor_save"),
    path('manage_student', viewsAdmin.manage_student, name="manage_student"),
    path('edit_student/<str:stud_id>/', viewsAdmin.edit_student, name="edit_student"),
    path('edit_student_save', viewsAdmin.edit_student_save, name="edit_student_save"),


    # path('signup/', views.signup, name="signup"),

    path('student_home', viewsStudent.student_home, name="student_home"),


    path('supervisor_home', viewsSupervisor.supervisor_home, name="supervisor_home")


]