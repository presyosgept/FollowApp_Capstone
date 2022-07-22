"""counseling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.views.generic import TemplateView

from followapp.views import(
    loginPage,
    signup,
    logoutUser,
    register,
    verification_code,
    home,

    # admin
    admin_home_view,
    upload_faculty,
    upload_subject_offerings,
    upload_student,
    upload_student_load,

    view_subject,
    view_school,
    view_department,
    view_faculty,
    view_counselor,
    view_subject_offerings,
    view_degree_program,
    view_student,
    view_student_load,


    view_student_detail,
    view_faculty_detail,

    edit_department,
    edit_subject,
    edit_school,
    edit_degree_program,

    search_student,
    search_faculty,

    view_faculty_with_load,
    search_faculty_with_load,
    view_student_with_load,
    search_student_with_load,

    # director
    director_home_view,
    list_degree_program,
    assign_counselor,

    # counselor
    counselor_home_view,

    # teacher
    teacher_home_view,
    student_list_enrolled,

    # student
    student_home_view,
    student_add_information,
    edit_information,

)


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', signup, name='signup'),
    path('register/', register, name='register'),
    path('verification_code/', verification_code, name="verification_code"),

    # admin
    path('head/', admin_home_view, name="admin_home_view"),
    path('admin/upload_faculty', upload_faculty, name="upload_faculty"),
    path('admin/upload_subject_offerings',
         upload_subject_offerings, name="upload_subject_offerings"),
    path('admin/upload_student', upload_student, name="upload_student"),
    path('admin/upload_student_load',
         upload_student_load, name="upload_student_load"),
    path('admin/view_subject', view_subject, name="view_subject"),
    path('admin/view_school', view_school, name="view_school"),
    path('admin/view_department', view_department, name="view_department"),
    path('admin/view_faculty', view_faculty, name="view_faculty"),
    path('admin/view_counselor', view_counselor, name="view_counselor"),
    path('admin/view_subject_offerings',
         view_subject_offerings, name="view_subject_offerings"),
    path('admin/view_degree_program',
         view_degree_program, name="view_degree_program"),
    path('admin/view_student', view_student, name="view_student"),
    path('admin/view_student_load',
         view_student_load, name="view_student_load"),

    path('admin/edit_department/<str:code>',
         edit_department, name="edit_department"),
    path('admin/edit_subject/<str:code>',
         edit_subject, name="edit_subject"),
    path('admin/edit_school/<str:name>',
         edit_school, name="edit_school"),
    path('admin/edit_degree_program/<str:code>',
         edit_degree_program, name="edit_degree_program"),

    path('admin/search_faculty/<str:search>',
         search_faculty, name="search_faculty"),
    path('admin/search_student/<str:search>',
         search_student, name="search_student"),


    path('admin/view_faculty_with_load',
         view_faculty_with_load, name="view_faculty_with_load"),
    path('admin/search_faculty_with_load/<str:search>',
         search_faculty_with_load, name="search_faculty_with_load"),
    path('admin/view_student_with_load',
         view_student_with_load, name="view_student_with_load"),
    path('admin/search_student_with_load/<str:search>',
         search_student_with_load, name="search_student_with_load"),


    path('admin/view_faculty_detail/<str:faculty_id>',
         view_faculty_detail, name="view_faculty_detail"),
    path('admin/view_student_detail/<str:student_number>',
         view_student_detail, name="view_student_detail"),


    # director
    path('director/', director_home_view, name="director_home_view"),
    path('director/list_degree_program',
         list_degree_program, name="list_degree_program"),
    path('director/assign_counselor/<str:code>',
         assign_counselor, name="assign_counselor"),
    # counselor
    path('counselor/', counselor_home_view, name="counselor_home_view"),


    # teacher
    path('teacher/', teacher_home_view, name="teacher_home_view"),
    path('teacher/student_list_enrolled/<str:offer_no>',
         student_list_enrolled, name="student_list_enrolled"),

    # student
    path('student/', student_home_view, name="student_home_view"),
    path('student_add_information/', student_add_information,
         name="student_add_information"),
    path('student/edit_information', edit_information, name="edit_information"),

    path('admin/', admin.site.urls),
]
