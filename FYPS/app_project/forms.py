from django import forms

from app_project.models import Programs, Sections


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    roll_no = forms.IntegerField(max_value=1000000, widget=forms.NumberInput(attrs={"class": "form-control"}) )
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    program_list = []
    try:
        programs = Programs.objects.all()
        for program in programs:
            small_program = (program.id, program.program_name)
            program_list.append(small_program)
    except:
        program_list = []

    section_list = []
    try:
        sections = Sections.objects.all()
        for section in sections:
            small_section = (section.id, section.section_name)
            section_list.append(small_section)
    except:
        section_list = []
    # course_list=[]

    # session_list = []
    # try:
    #     sessions = SessionYearModel.object.all()
    #
    #     for ses in sessions:
    #         small_ses = (ses.id, str(ses.session_start_year) + "   TO  " + str(ses.session_end_year))
    #         session_list.append(small_ses)
    # except:
    #     session_list = []
    #
    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    semester_choice = (
        (4, 4),
        (6, 8)
    )

    program = forms.ChoiceField(label="Program", choices=program_list, widget=forms.Select(attrs={"class": "form-control"}))
    section = forms.ChoiceField(label="Section", choices=section_list, widget=forms.Select(attrs={"class": "form-control"}))
    semester = forms.ChoiceField(label="Semester", choices=semester_choice, widget=forms.Select(attrs={"class": "form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    session_start = forms.DateField(label="Session Year start", widget=DateInput(attrs={"class": "form-control"}) )
    session_end = forms.DateField(label="Session Year end", widget=DateInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50, widget=forms.FileInput(attrs={"class": "form-control"}))
    
    
class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    roll_no = forms.IntegerField(max_value=1000000, widget=forms.NumberInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    program_list = []
    try:
        programs = Programs.objects.all()
        for program in programs:
            small_program = (program.id, program.program_name)
            program_list.append(small_program)
    except:
        program_list = []

    section_list = []
    try:
        sections = Sections.objects.all()
        for section in sections:
            small_section = (section.id, section.section_name)
            section_list.append(small_section)
    except:
        section_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    semester_choice = (
        (4, 4),
        (6, 8)
    )

    program = forms.ChoiceField(label="Program", choices=program_list,
                                widget=forms.Select(attrs={"class": "form-control"}))
    section = forms.ChoiceField(label="Section", choices=section_list,
                                widget=forms.Select(attrs={"class": "form-control"}))
    semester = forms.ChoiceField(label="Semester", choices=semester_choice,
                                 widget=forms.Select(attrs={"class": "form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_choice,
                               widget=forms.Select(attrs={"class": "form-control"}))
    session_start = forms.DateField(label="Session Year start", widget=DateInput(attrs={"class": "form-control"}))
    session_end = forms.DateField(label="Session Year end", widget=DateInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}), required=False)


    # email = forms.EmailField(label="Email", max_length=50,
    #                          widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))
    # password = forms.CharField(label="Password", max_length=50,
    #                            widget=forms.PasswordInput(attrs={"class": "form-control"}))
    # first_name = forms.CharField(label="First Name", max_length=50,
    #                              widget=forms.TextInput(attrs={"class": "form-control"}))
    # last_name = forms.CharField(label="Last Name", max_length=50,
    #                             widget=forms.TextInput(attrs={"class": "form-control"}))
    # username = forms.CharField(label="Username", max_length=50,
    #                            widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    # address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    # course_list = []
    # try:
    #     courses = Courses.objects.all()
    #     for course in courses:
    #         small_course = (course.id, course.course_name)
    #         course_list.append(small_course)
    # except:
    #     course_list = []
    # # course_list=[]
    #
    # session_list = []
    # try:
    #     sessions = SessionYearModel.object.all()
    #
    #     for ses in sessions:
    #         small_ses = (ses.id, str(ses.session_start_year) + "   TO  " + str(ses.session_end_year))
    #         session_list.append(small_ses)
    # except:
    #     session_list = []
    #
    # gender_choice = (
    #     ("Male", "Male"),
    #     ("Female", "Female")
    # )
    #
    # program = forms.ChoiceField(label="Program", choices=course_list,
    #                            widget=forms.Select(attrs={"class": "form-control"}))
    # section = forms.ChoiceFild(label="Program", choices=course_list,
    #                            widget=forms.Select(attrs={"class": "form-control"}))
    # sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    # session_year_id = forms.ChoiceField(label="Session Year", choices=session_list,
    #                                     widget=forms.Select(attrs={"class": "form-control"}))
    # profile_pic = forms.FileField(label="Profile Pic", max_length=50,
    #                               widget=forms.FileInput(attrs={"class": "form-control"}))