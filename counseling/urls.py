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


    path('admin/', admin.site.urls),
]
