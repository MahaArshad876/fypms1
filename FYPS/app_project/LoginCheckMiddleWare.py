from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename = view_func.__module__
        print(modulename)
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "app_project.viewsAdmin":
                    pass
                elif modulename == "app_project.views" or modulename == "django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "app_project.viewsSupervisor" or modulename == "app_project.EditResultVIewClass":
                    pass
                elif modulename == "app_project.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("supervisor_home"))
            elif user.user_type == "3":
                if modulename == "app_project.viewsStudent" or modulename == "django.views.static":
                    pass
                elif modulename == "app_project.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse(
                    "doLogin") or modulename == "django.contrib.auth.views" or modulename == "app_project.views" or modulename == "django.contrib.admin.sites":
                pass
            else:
                return HttpResponseRedirect(reverse("login"))