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
    upload_semester,
    upload_offerings,
    upload_subject,
    upload_school,
    upload_department,
    upload_faculty,
    upload_counselor,
    upload_subject_offerings,
    upload_degree_program,
    upload_student,
    upload_student_load,

    view_semester,
    view_offerings,
    view_subject,
    view_school,
    view_department,
    view_faculty,
    view_counselor,
    view_subject_offerings,
    view_degree_program,
    view_student,
    view_student_load,
    edit_department,
    edit_subject,

    # director
    director_home_view,

    # counselor
    counselor_home_view,

    # teacher
    teacher_home_view

    # student

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
    path('admin/upload_semester', upload_semester, name="upload_semester"),
    path('admin/upload_offerings', upload_offerings, name="upload_offerings"),
    path('admin/upload_subject', upload_subject, name="upload_subject"),
    path('admin/upload_school', upload_school, name="upload_school"),
    path('admin/upload_department', upload_department, name="upload_department"),
    path('admin/upload_faculty', upload_faculty, name="upload_faculty"),
    path('admin/upload_counselor', upload_counselor, name="upload_counselor"),
    path('admin/upload_subject_offerings',
         upload_subject_offerings, name="upload_subject_offerings"),
    path('admin/upload_degree_program',
         upload_degree_program, name="upload_degree_program"),
    path('admin/upload_student', upload_student, name="upload_student"),
    path('admin/upload_student_load',
         upload_student_load, name="upload_student_load"),
    path('admin/view_semester', view_semester, name="view_semester"),
    path('admin/view_offerings', view_offerings, name="view_offerings"),
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


    # director
    path('director/', director_home_view, name="director_home_view"),

    # counselor
    path('counselor/', counselor_home_view, name="counselor_home_view"),


    # teacher
    path('teacher/', teacher_home_view, name="teacher_home_view"),

    path('admin/', admin.site.urls),
]
