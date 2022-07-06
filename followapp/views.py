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

from .forms import CreateUserForm, AccountsForm, VerificationForm, AccountCreatedForm

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
                auth_token = 'c2bea526026f45859efe73f62f35b2cb'
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
                    if username == user.studnumber:
                        flag = 1
                for user in qs_faculty:
                    if username == user.employee_id:
                        flag = 1
                if flag == 1:
                    account_sid = 'AC47090e11c4e65aba8e1ce9f75e7522c5'
                    auth_token = 'c2bea526026f45859efe73f62f35b2cb'
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
                            if student.role == 'learner':
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
                                if teacher.role == 'teacher':
                                    request.session['username'] = username
                                    flag = 2
                                elif teacher.role == 'counselor':
                                    request.session['username'] = username
                                    flag = 3
                                elif teacher.role == 'director':
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
def upload_semester(request):
    try:
        semester = Semester.objects.all()
        if request.method == 'POST':
            SemesterResource()
            dataset = Dataset()
            new_sem = request.FILES['myfile']
            imported_data = dataset.load(new_sem.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_sem)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 2):
                for data in imported_data:
                    value = Semester(
                        data[0],
                        data[1],
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_semester.html", {"sem": semester})


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
def upload_subject(request):
    try:
        subject = Subject.objects.all()
        if request.method == 'POST':
            SubjectResource()
            dataset = Dataset()
            new_subject = request.FILES['myfile']
            imported_data = dataset.load(new_subject.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_subject)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 3):
                for data in imported_data:
                    value = Subject(
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
    return render(request, "admin/upload_subject.html", {"subject": subject})


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
def upload_department(request):
    try:
        department = Department.objects.all()
        if request.method == 'POST':
            DepartmentResource()
            dataset = Dataset()
            new_department = request.FILES['myfile']
            imported_data = dataset.load(new_department.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_department)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 3):
                for data in imported_data:
                    value = Department(
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
    return render(request, "admin/upload_department.html", {"department": department})


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

            if(col == 6):
                for data in imported_data:
                    value = Faculty(
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
            new_subject_offerings = request.FILES['myfile']
            imported_data = dataset.load(
                new_subject_offerings.read(), format='xlsx')
            wb_obj = openpyxl.load_workbook(new_subject_offerings)
            sheet_obj = wb_obj.active
            col = sheet_obj.max_column
            row = sheet_obj.max_row

            if(col == 10):
                for data in imported_data:
                    value = SubjectOfferings(
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
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
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

            if(col == 4):
                for data in imported_data:
                    value = DegreeProgram(
                        data[0],
                        data[1],
                        data[2],
                        data[3]
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
                    value = Studentload(
                        data[0],
                        data[1],
                        data[2],
                        data[3]
                    )
                    value.save()
                messages.info(request, 'Successfully Added')
            else:
                messages.info(request, 'Failed to Add the Data')
    except Exception:
        messages.info(request, 'Please Choose File')
    return render(request, "admin/upload_student_load.html", {"student_load": student_load})
# admin
