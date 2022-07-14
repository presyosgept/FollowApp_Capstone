from django.shortcuts import render

from twilio.rest import Client
from json import encoder
from typing import Counter
from django.db.models.fields import TimeField
from django.http import HttpResponse, request
from django.http.response import Http404, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Max, Min
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# from .utilities import create_notification, create_feedback
from django.views import generic
from django.utils import timezone
from datetime import date, datetime, timedelta

import datetime as dt
from tablib import Dataset

from django.shortcuts import render
from django.shortcuts import get_object_or_404
import openpyxl

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
import random
from django.contrib.auth.models import User

from .models import Semester, Offerings, Subject, School, Department, Faculty, Counselor, SubjectOfferings, DegreeProgram, Student, Studentload
from .models import AccountCreated
from .resources import SemesterResource, OfferingsResource, SubjectResource, SchoolResource, DepartmentResource, FacultyResource, CounselorResource, SubjectOfferingsResource, DegreeProgramResource, StudentResource, StudentloadResource

from .forms import AssignCounselorForm, CreateUserForm, AccountsForm, VerificationForm, AccountCreatedForm, EditDepartmentForm, EditSubjectForm

# global variables
counselorNotif = 0
studentNotif = 0
teacherNotif = 0
count = 0
count1 = 0
formm = AccountsForm()
feedback_id = 0
global sem
global sy
global dep
global school
global filterStartDate
global filterEndData
global Search


def register(request):
    form = AccountCreatedForm()
    if request.method == 'POST':
        char = '1234567890'
        for x in range(0, 1):
            code = ''
            for x in range(0, 8):
                code_char = random.choice(char)
                code = code + code_char
        username = request.POST.get('id_number')
        email = request.POST.get('email')
        checker = email.find('+63')
        if checker == 0:
            qs_faculty = Faculty.objects.all()
            qs_student = Student.objects.all()
            qs_acc = AccountCreated.objects.all()

            if username == 'followapp':
                account_sid = 'AC47090e11c4e65aba8e1ce9f75e7522c5'
                auth_token = '6a4c0f4f25343f30f14f9adb73f858f7'
                client = Client(account_sid, auth_token)
                body = 'This is your VERIFICATION CODE FOR FOLLOWAPP: ' + code
                message = client.messages.create(
                    to=email, from_='+15166045607', body=body)
                print(message.sid)
                value = AccountCreated(
                    id_number=username, email=email, password=code)
                value.save()
                return redirect('verification_code')

            exist = 0
            for acc in qs_acc:
                if username == acc.id_number:
                    exist = 1

            if exist == 0:
                flag = 0
                for user in qs_student:
                    if username == user.student_number:
                        flag = 1
                for user in qs_faculty:
                    if username == user.faculty_id:
                        flag = 1
                if flag == 1:
                    account_sid = 'AC47090e11c4e65aba8e1ce9f75e7522c5'
                    auth_token = '6a4c0f4f25343f30f14f9adb73f858f7'
                    client = Client(account_sid, auth_token)
                    body = 'This is your VERIFICATION CODE FOR FOLLOWAPP: ' + code
                    message = client.messages.create(
                        to=email, from_='+15166045607', body=body)
                    print(message.sid)
                    value = AccountCreated(
                        id_number=username, email=email, password=code)
                    value.save()
                    messages.info(request, "Check SMS for Code")
                    return redirect('verification_code')
                else:
                    messages.info(request, "Account Not Valid")
            else:
                messages.info(request, "Account Already Existed")
        else:
            messages.info(request, "Number should start +63")
    else:
        AccountsForm()

    return render(request, 'register.html', {'form': form})


def verification_code(request):
    form = VerificationForm()
    code = request.POST.get('code')
    if request.method == 'POST':
        qs_account = AccountCreated.objects.all()
        flag = 0
        for vcode in qs_account:
            if (code == vcode.password):
                flag = 1

        if(flag == 1):
            return redirect('signup')
        else:
            VerificationForm()
            messages.info(request, 'Invalid Code')
    else:
        VerificationForm()

    return render(request, 'verification.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            qs_account = AccountCreated.objects.all()
            exist = 0
            for user in qs_account:
                if user.id_number == username:
                    exist = 1
            if (exist == 1):
                flag = 0
                qs = Student.objects.all()
                for student in qs:
                    if student.student_number == username:
                        flag = 1
                        stud = Student.objects.get(student_number=username)
                        # studentInfo = StudentInfo(firstname=stud.firstname,
                        #                           lastname=stud.lastname, middlename=stud.middlename, studnumber=stud.studnumber,
                        #                           degree_program=stud.degree_program, year=stud.year, student_email=stud.student_email)
                        # studentInfo.save()
                if flag == 1:
                    form = CreateUserForm(request.POST)
                    if form.is_valid():
                        form.save()
                        user = form.cleaned_data.get('username')
                        messages.info(
                            request, 'Student Account was created for ' + user)
                        return redirect('login')
                elif flag == 0:
                    qs = Faculty.objects.all()
                    for faculty in qs:
                        if faculty.faculty_id == username:
                            form = CreateUserForm(request.POST)
                            if form.is_valid():
                                form.save()
                                user = form.cleaned_data.get('username')
                                messages.info(
                                    request, 'Account was created for ' + user)
                                return redirect('login')

                if username == 'followapp':
                    form = CreateUserForm(request.POST)
                    if form.is_valid():
                        form.save()
                        user = form.cleaned_data.get('username')
                        messages.info(
                            request, 'Admin Account was created for ' + user)
                        return redirect('login')

                messages.info(request, 'Check Credentials Account Not Created')

            else:
                messages.info(request, 'Check Credentials Account Not Created')

    return render(request, 'signup.html', {'form': form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if request.method == 'POST':
                    flag = 0
                    username = request.POST.get('username')
                    qs = Student.objects.all()
                    for student in qs:
                        if student.student_number == username:
                            if student.role == 'Learner':
                                flag = 1
                    if flag == 1:
                        return redirect('student_home_view')
                        # request.session['username'] = username
                        # # return redirect('student_home_view')
                        # check = StudentInfo.objects.all()
                        # if check is not None:
                        #     stud = StudentInfo.objects.get(studnumber=username)
                        #     if stud.status == 'undone':
                        #         return redirect('student_add_info')
                        #     else:
                        #         return redirect('student_home_view')
                        # else:
                        #     return redirect('student_add_info')

                    else:
                        qs = Faculty.objects.all()
                        for teacher in qs:
                            if teacher.faculty_id == username:
                                if teacher.role == 'Teacher':
                                    request.session['username'] = username
                                    flag = 2
                                elif teacher.role == 'Counselor':
                                    request.session['username'] = username
                                    flag = 3
                                elif teacher.role == 'Director':
                                    request.session['username'] = username
                                    flag = 4
                    if flag == 2:
                        return redirect('teacher_home_view')
                    if flag == 3:
                        return redirect('counselor_home_view')
                    if flag == 4:
                        return redirect('director_home_view')
                    if username == 'followapp':
                        return redirect('admin_home_view')
            else:
                messages.info(request, 'Username or Password is Incorrect')

        return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request, *args, **kwargs):
    return render(request, "welcomepage.html", {})


# admin


@login_required(login_url='login')
def admin_home_view(request, *args, **kwargs):
    return render(request, "admin/home.html", {})


@login_required(login_url='login')
def view_offerings(request, *args, **kwargs):
    offerings = Offerings.objects.all()
    return render(request, "admin/view_offerings.html", {"offerings": offerings})


@login_required(login_url='login')
def view_subject(request, *args, **kwargs):
    subject = Subject.objects.all()
    return render(request, "admin/view_subject.html", {"subject": subject})


@login_required(login_url='login')
def edit_subject(request, code):
    subject = Subject.objects.get(subject_code=code)
    edit_form = EditSubjectForm()
    if request.method == "POST":
        edit_form = EditSubjectForm(request.POST)
        if edit_form.is_valid():
            new_units = edit_form['units'].value()
            edit = Subject.objects.get(subject_code=code)
            edit.units = new_units
            edit.save()
            subject = Subject.objects.get(subject_code=code)
    return render(request, "admin/edit_subject.html", {'subject': subject, 'edit_form': edit_form})


@login_required(login_url='login')
def view_school(request, *args, **kwargs):
    school = School.objects.all()
    return render(request, "admin/view_school.html", {"school": school})


@login_required(login_url='login')
def view_department(request, *args, **kwargs):
    department = Department.objects.all()
    return render(request, "admin/view_department.html", {'department': department})


@login_required(login_url='login')
def edit_department(request, code):
    department = Department.objects.get(department_code=code)
    edit_form = EditDepartmentForm(instance=department)
    if request.method == "POST":
        edit_form = EditDepartmentForm(request.POST, instance=department)
        if edit_form.is_valid():
            new_department_name = edit_form['department_name'].value()
            new_school_code = edit_form['school_code'].value()
            get_school_code = School.objects.get(school_code=new_school_code)
            edit = Department.objects.get(department_code=code)
            edit.department_name = new_department_name
            edit.save()
            edit.school_code = get_school_code
            edit.save()
    return render(request, "admin/edit_department.html", {'department': department, 'edit_form': edit_form})


@login_required(login_url='login')
def view_faculty(request, *args, **kwargs):
    faculty = Faculty.objects.all()
    return render(request, "admin/view_faculty.html", {'faculty': faculty})


@login_required(login_url='login')
def view_counselor(request, *args, **kwargs):
    counselor = Faculty.objects.filter(role='Counselor')
    return render(request, "admin/view_counselor.html", {'counselor': counselor})


@login_required(login_url='login')
def view_subject_offerings(request, *args, **kwargs):
    subject_offerings = SubjectOfferings.objects.all()
    return render(request, "admin/view_subject_offerings.html", {'subject_offerings': subject_offerings})


@login_required(login_url='login')
def view_degree_program(request, *args, **kwargs):
    degree_program = DegreeProgram.objects.all()
    return render(request, "admin/view_degree_program.html", {'degree_program': degree_program})


@login_required(login_url='login')
def view_student(request, *args, **kwargs):
    student = Student.objects.all()
    return render(request, "admin/view_student.html", {'student': student})


@login_required(login_url='login')
def view_student_load(request, *args, **kwargs):
    student_load = Studentload.objects.all()
    return render(request, "admin/view_student_load.html", {'student_load': student_load})


@login_required(login_url='login')
def upload_offerings(request):
    try:
        offerings = Offerings.objects.all()
        if request.method == 'POST':
            OfferingsResource()
            dataset = Dataset()
            new_offerings = request.FILES['myfile']
            imported_data = dataset.load(new_offerings.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_offerings)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 6):
                for data in imported_data:
                    value = Offerings(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_offerings.html", {"offerings": offerings})


@login_required(login_url='login')
def upload_school(request):
    try:
        school = School.objects.all()
        if request.method == 'POST':
            SchoolResource()
            dataset = Dataset()
            new_school = request.FILES['myfile']
            imported_data = dataset.load(new_school.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_school)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 2):
                for data in imported_data:
                    value = School(
                        data[0],
                        data[1]
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_school.html", {"school": school})


@login_required(login_url='login')
def upload_faculty(request):
    try:
        faculty = Faculty.objects.all()
        if request.method == 'POST':
            FacultyResource()
            dataset = Dataset()
            new_faculty = request.FILES['myfile']
            imported_data = dataset.load(new_faculty.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_faculty)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 7):
                for data in imported_data:
                    check_faculty = Faculty.objects.all()
                    flag_faculty = 0
                    flag_depa = 0
                    check_depa = Department.objects.all()
                    for obj in check_depa:
                        if obj.department_code == data[5]:
                            flag_depa = 1
                    if flag_depa == 0:
                        depa = Department(department_code=data[6])
                        depa.save()
                    for obj in check_faculty:
                        if obj.faculty_id == str(data[0]):
                            flag_faculty = 1
                            id = obj.faculty_id
                    if flag_faculty == 0:
                        depa = Department.objects.get(
                            department_code=str(data[6]))
                        value = Faculty(
                            faculty_id=str(data[0]),
                            lastname=data[1],
                            firstname=data[2],
                            middlename=data[3],
                            email=data[4],
                            role=data[5],
                            department_code=depa
                        )
                        value.save()
                    else:
                        check = Faculty.objects.get(faculty_id=id)
                        check.lastname = data[1]
                        check.save()
                        check.firstname = data[2]
                        check.save()
                        check.middlename = data[3]
                        check.save()
                        check.email = data[4]
                        check.save()
                        check.role = data[5]
                        check.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_faculty.html", {"faculty": faculty})


@login_required(login_url='login')
def upload_counselor(request):
    try:
        counselor = Counselor.objects.all()
        if request.method == 'POST':
            CounselorResource()
            dataset = Dataset()
            new_counselor = request.FILES['myfile']
            imported_data = dataset.load(new_counselor.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_counselor)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 3):
                for data in imported_data:
                    value = Counselor(
                        data[0],
                        data[1],
                        data[2]
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_counselor.html", {"counselor": counselor})


@login_required(login_url='login')
def upload_subject_offerings(request):
    try:
        subject_offerings = SubjectOfferings.objects.all()
        if request.method == 'POST':
            SubjectOfferingsResource()
            dataset = Dataset()
            new_sem = request.FILES['myfile']
            imported_data = dataset.load(new_sem.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_sem)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 9):
                for data in imported_data:
                    check_depa = Department.objects.all()
                    check_faculty = Faculty.objects.all()
                    check_offerings = Offerings.objects.all()
                    check_subject = Subject.objects.all()
                    is_depa = bool(check_depa)
                    is_faculty = bool(check_faculty)
                    is_offerings = bool(check_offerings)
                    is_subject = bool(check_subject)

                    if is_depa:
                        if data[7] not in check_depa:
                            depa = Department(department_code=data[7])
                            depa.save()
                    else:
                        depa = Department(department_code=data[7])
                        depa.save()

                    if is_faculty:
                        if str(data[8]) not in check_faculty:
                            depa = Department.objects.get(
                                department_code=data[7])
                            faculty = Faculty(faculty_id=str(
                                data[8]), department_code=depa)
                            faculty.save()
                    else:
                        depa = Department.objects.get(
                            department_code=data[7])
                        faculty = Faculty(faculty_id=str(
                            data[8]), department_code=depa)
                        faculty.save()

                    flag = 0
                    if is_offerings:
                        for obj in check_offerings:
                            if str(data[0]) == obj.offer_no and str(data[5]) == obj.sem_id:
                                flag = 1
                        if flag == 0:
                            offerings = Offerings(offer_no=str(data[0]), days=str(data[3]), school_time=str(
                                data[4]), sem_id=str(data[5]), academic_year=str(data[6]))
                            offerings.save()
                    else:
                        offerings = Offerings(
                            offer_no=str(data[0]), days=str(data[3]), school_time=str(data[4]), sem_id=str(data[5]), academic_year=str(data[6]))
                        offerings.save()

                    if is_subject:
                        if data[1] not in check_subject:
                            subject = Subject(
                                subject_code=data[1], subject_title=data[2])
                            subject.save()
                    else:
                        subject = Subject(
                            subject_code=data[1], subject_title=data[2])
                        subject.save()

                for data in imported_data:
                    print(data[0])
                    get_offer_no = Offerings.objects.get(
                        offer_no=str(data[0]), sem_id=str(data[5]))
                    get_subject_code = Subject.objects.get(
                        subject_code=data[1])
                    get_department_code = Department.objects.get(
                        department_code=data[7])
                    get_faculty_id = Faculty.objects.get(
                        faculty_id=str(data[8]))
                    value = SubjectOfferings(
                        offer_no=get_offer_no,
                        subject_code=get_subject_code,
                        subject_title=data[2],
                        school_days=str(data[3]),
                        school_time=str(data[4]),
                        sem_id=str(data[5]),
                        academic_year=str(data[6]),
                        department_code=get_department_code,
                        faculty_id=get_faculty_id
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception as e:
        print('helo', e)
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_subject_offerings.html", {"subject_offerings": subject_offerings})


@login_required(login_url='login')
def upload_degree_program(request):
    try:
        degree_program = DegreeProgram.objects.all()
        if request.method == 'POST':
            DegreeProgramResource()
            dataset = Dataset()
            new_degree_program = request.FILES['myfile']
            imported_data = dataset.load(
                new_degree_program.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_degree_program)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 3):
                for data in imported_data:
                    value = DegreeProgram(
                        data[0],
                        data[1],
                        data[2]
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_degree_program.html", {"degree_program": degree_program})


@login_required(login_url='login')
def upload_student(request):
    try:
        student = Student.objects.all()
        if request.method == 'POST':
            StudentResource()
            dataset = Dataset()
            new_student = request.FILES['myfile']
            imported_data = dataset.load(
                new_student.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_student)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 13):
                for data in imported_data:
                    value = Student(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                        data[8],
                        data[9],
                        data[10],
                        data[11],
                        data[12],
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_student.html", {"student": student})


@login_required(login_url='login')
def upload_student_load(request):
    try:
        student_load = Studentload.objects.all()
        if request.method == 'POST':
            StudentloadResource()
            dataset = Dataset()
            new_student_load = request.FILES['myfile']
            imported_data = dataset.load(
                new_student_load.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_student_load)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 4):
                for data in imported_data:
                    get_student_number = Student.objects.get(
                        student_number=str(data[0]))
                    get_offer_no = Offerings.objects.get(
                        offer_no=str(data[1]), sem_id=str(data[2]))
                    value = Studentload(
                        student_number=get_student_number,
                        offer_no=get_offer_no,
                        sem_id=str(data[2]),
                        academic_year=str(data[3])
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception as e:
        print('hi', e)
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_student_load.html", {"student_load": student_load})
# admin


# director
@login_required(login_url='login')
def director_home_view(request, *args, **kwargs):
    user = request.session.get('username')
    director_name = Faculty.objects.get(faculty_id=user)
    return render(request, "director/home.html", {"form": director_name})


@login_required(login_url='login')
def list_degree_program(request, *args, **kwargs):
    user = request.session.get('username')
    director_name = Faculty.objects.get(faculty_id=user)
    degree_program = DegreeProgram.objects.all()
    return render(request, "director/list_degree_program.html", {"form": director_name, 'degree_program': degree_program})


@login_required(login_url='login')
def assign_counselor(request, code):
    user = request.session.get('username')
    director_name = Faculty.objects.get(faculty_id=user)
    degree_program = DegreeProgram.objects.get(program_code=code)
    edit_form = AssignCounselorForm()
    if request.method == "POST":
        edit_form = AssignCounselorForm(request.POST)
        if edit_form.is_valid():
            new_faculty = edit_form['faculty'].value()
            get_counselor = Faculty.objects.get(faculty_id=new_faculty)
            edit = DegreeProgram.objects.get(program_code=code)
            edit.faculty_id = get_counselor
            edit.save()
            degree_program = DegreeProgram.objects.get(program_code=code)
    return render(request, "director/assign_counselor.html", {"form": director_name, 'degree_program': degree_program, 'edit_form': edit_form})

# director


# counselor
@login_required(login_url='login')
def counselor_home_view(request, *args, **kwargs):
    user = request.session.get('username')
    counselor_name = Faculty.objects.get(faculty_id=user)
    return render(request, "counselor/home.html", {"form": counselor_name})
# counselor


# teacher
@login_required(login_url='login')
def teacher_home_view(request, *args, **kwargs):
    user = request.session.get('username')
    teacher_name = Faculty.objects.get(faculty_id=user)
    return render(request, "teacher/teacher_home.html",  {"form": teacher_name})
# teacher
