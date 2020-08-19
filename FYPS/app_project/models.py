from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Supervisor"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Supervisor(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, max_length=10)
    gender = models.CharField(max_length=225)
    profile_pic = models.FileField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Programs(models.Model):
    id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Sections(models.Model):
    id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=225)
    program_id = models.ForeignKey(Programs, on_delete=models.CASCADE,default=1)
    supervisor_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    roll_no = models.IntegerField(blank=True, null=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, max_length=10)
    gender = models.CharField(max_length=225)
    profile_pic = models.FileField()
    address = models.TextField()
    program_id = models.ForeignKey(Programs, on_delete=models.DO_NOTHING, null=True)
    semester = models.IntegerField(blank=True, null=True)
    section_id = models.ForeignKey(Sections, on_delete=models.DO_NOTHING, null=True)
    session_start_at = models.DateField()
    session_end_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ApplyProjectApproval(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    apply_date = models.CharField(max_length=255)
    project_title = models.CharField(max_length=225)
    abstract = models.TextField()
    conclusion = models.TextField()
    approval_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class StudMessageAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    student_message = models.TextField()
    admin_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class LeaveSupervisor(models.Model):
    id = models.AutoField(primary_key=True)
    supervisor_id = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class SupMessageAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    supervisor_id = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    message_admin = models.TextField()
    message_reply =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Supervisor.objects.create(admin=instance, )
        if instance.user_type == 3:
            Students.objects.create(admin=instance, program_id=Programs.objects.get(id=1), profile_pic="", session_start_at="2020-01-01", session_end_at="2021-01-01", address="")


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.supervisor.save()
    if instance.user_type == 3:
        instance.students.save()