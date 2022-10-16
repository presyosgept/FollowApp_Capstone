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
from django.urls import include, path
from django.urls import re_path as url
from django.views.generic import TemplateView
from followapp.views import (  # admin; director; counselor; teacher; student; api
    admin_home_view,
    another_counselor_view_schedule,
    another_student_view_schedule,
    assign_counselor,
    counselor_feedback_student,
    counselor_home_view,
    counselor_notification_detail,
    counselor_notifications,
    counselor_set_schedule,
    counselor_videocall,
    counselor_view_feedback,
    counselor_view_feedback_with_date,
    counselor_view_schedule,
    detail_referred_student,
    detail_referred_student_counselor,
    detail_referred_student_with_feedback,
    director_home_view,
    edit_degree_program,
    edit_department,
    edit_information,
    edit_school,
    home,
    list_degree_program,
    loginPage,
    logoutUser,
    per_counselor,
    per_degree_program,
    referral,
    register,
    search_faculty,
    search_faculty_with_load,
    search_student,
    search_student_enroll,
    search_student_with_load,
    set_active_year,
    signup,
    student_add_information,
    student_history,
    student_home_view,
    student_list_enrolled,
    student_notification_detail,
    student_notifications,
    student_set_schedule,
    student_videocall,
    student_view_schedule,
    teacher_home_view,
    teacher_notification_detail,
    teacher_notifications,
    teacher_view_referred_students,
    upload_faculty,
    upload_student,
    upload_student_load,
    upload_subject_offerings,
    verification_code,
    view_counselor,
    view_degree_program,
    view_department,
    view_faculty,
    view_faculty_detail,
    view_faculty_with_load,
    view_pending_referred_students,
    view_referred_students,
    view_school,
    view_stat_by_counselor,
    view_stat_by_counselor_with_date,
    view_stat_by_degree_program,
    view_stat_by_degree_program_with_date,
    view_student,
    view_student_detail,
    view_student_load,
    view_student_with_load,
    view_subject,
    view_subject_offerings,
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
     path('admin/set_active_year', set_active_year, name="set_active_year"),
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
    path('director/per_degree_program',
         per_degree_program, name="per_degree_program"),
    path('director/view_stat_by_degree_program/<str:degree>',
         view_stat_by_degree_program, name="view_stat_by_degree_program"),
    path('director/per_counselor',
         per_counselor, name="per_counselor"),
    path('director/view_stat_by_counselor/<str:counselor_id>',
         view_stat_by_counselor, name="view_stat_by_counselor"),
    path('director/view_stat_by_counselor_with_date/<str:counselor_id>', view_stat_by_counselor_with_date,
         name="view_stat_by_counselor_with_date"),
    path('director/view_stat_by_degree_program_with_date/<str:degree>', view_stat_by_degree_program_with_date,
         name="view_stat_by_degree_program_with_date"),




    # counselor
    path('counselor/', counselor_home_view, name="counselor_home_view"),
    path('counselor/view_referred_students',
         view_referred_students, name="view_referred_students"),
    path('counselor/view_pending_referred_students',
         view_pending_referred_students, name="view_pending_referred_students"),
    path('counselor/detail_referred_student_counselor/?P:<int:id>', detail_referred_student_counselor,
         name='detail_referred_student_counselor'),
    path('counselor/counselor_set_schedule',
         counselor_set_schedule, name="counselor_set_schedule"),
    path('counselor/counselor_notifications',
         counselor_notifications, name="counselor_notifications"),
    path('counselor/counselor_notification_detail/?P:<int:id>', counselor_notification_detail,
         name='counselor_notification_detail'),
    path('counselor/counselor_feedback_student/?P:<int:id>',
         counselor_feedback_student, name='counselor_feedback_student'),
    path('counselor/counselor_view_feedback',
         counselor_view_feedback, name="counselor_view_feedback"),
    path('counselor/counselor_view_feedback_with_date/<str:date>',
         counselor_view_feedback_with_date, name="counselor_view_feedback_with_date"),
    path('counselor/detail_referred_student_with_feedback/?P:<int:id>', detail_referred_student_with_feedback,
         name='detail_referred_student_with_feedback'),
    path('counselor/counselor_view_schedule',
         counselor_view_schedule, name="counselor_view_schedule"),
    path('counselor/another_counselor_view_schedule',
         another_counselor_view_schedule, name="another_counselor_view_schedule"),
     path('counselor/counselor_videocall/<int:room_name>',
         counselor_videocall, name="counselor_videocall"),



    # teacher
    path('teacher/', teacher_home_view, name="teacher_home_view"),
    path('teacher/student_list_enrolled/<str:offer_no>',
         student_list_enrolled, name="student_list_enrolled"),
    path('teacher/teacher_view_referred_students/<str:status>',
         teacher_view_referred_students, name="teacher_view_referred_students"),
    path('teacher/detail_referred_student/?P:<int:id>', detail_referred_student,
         name='detail_referred_student'),
    path('teacher/referral/<str:studentReferredId>/<str:offer_no>', referral,
         name='referral'),
    path('teacher/teacher_notifications',
         teacher_notifications, name="teacher_notifications"),
    path('teacher/teacher_notification_detail/?P:<int:id>', teacher_notification_detail,
         name='teacher_notification_detail'),
path('admin/search_student_enroll/<str:search>/<str:offer_no>',
         search_student_enroll, name="search_student_enroll"),

    # student
    path('student/', student_home_view, name="student_home_view"),
    path('student_add_information/', student_add_information,
         name="student_add_information"),
    path('student/edit_information', edit_information, name="edit_information"),
    path('student/student_history', student_history, name="student_history"),
    path('student/student_notifications',
         student_notifications, name="student_notifications"),
    path('student/student_notification_detail/<str:status>/?P:<int:id>', student_notification_detail,
         name='student_notification_detail'),
    path('student/student_view_schedule',
         student_view_schedule, name="student_view_schedule"),
    path('student/another_student_view_schedule',
         another_student_view_schedule, name="another_student_view_schedule"),
    path('student/student_set_schedule',
         student_set_schedule, name="student_set_schedule"),
  path('student/student_videocall/<int:room_name>',
         student_videocall, name="student_videocall"),


    path('admin/', admin.site.urls),
]
