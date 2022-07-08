from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Semester, Offerings, Subject, School, Department, Faculty, Counselor, SubjectOfferings, DegreeProgram, Student, Studentload
from .models import AccountCreated
# admin.site.register(Semester)

admin.site.register(Semester)


class SemesterAdmin(ImportExportModelAdmin):
    list_display = ('sem_id', 'semester')


admin.site.register(Offerings)


class OfferingsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'offer_no', 'days', 'school_time',
                    'sem_id', 'academic_year')


admin.site.register(Subject)


class SubjectAdmin(ImportExportModelAdmin):
    list_display = ('subject_code', 'subject_title', 'units')


admin.site.register(School)


class SchoolAdmin(ImportExportModelAdmin):
    list_display = ('school_code', 'school_name')


admin.site.register(Department)


class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ('department_code', 'department_name', 'school_code')


admin.site.register(Faculty)


class FacultyAdmin(ImportExportModelAdmin):
    list_display = ('faculty_id', 'lastname', 'firstname',
                    'email', 'role', 'department_code')


admin.site.register(Counselor)


class CounselorAdmin(ImportExportModelAdmin):
    list_display = ('counselor_id', 'lastname', 'firstname')


admin.site.register(SubjectOfferings)


class SubjectOfferingsAdmin(ImportExportModelAdmin):
    list_display = ('offer_no', 'subject_code', 'subject_title', 'school_days',
                    'school_time', 'sem_id', 'academic_year', 'department_code', 'faculty_id')


admin.site.register(DegreeProgram)


class DegreeProgramAdmin(ImportExportModelAdmin):
    list_display = ('program_code', 'program_name',
                    'school_code', 'counselor_id')


admin.site.register(Student)


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('student_number', 'lastname', 'firstname', 'middlename', 'gender', 'avg_grade',
                    'IQ', 'birthdate', 'hometown', 'program_code', 'year',  'student_email', 'role')


admin.site.register(Studentload)


class StudentloadAdmin(ImportExportModelAdmin):
    list_display = ('student_number', 'offer_code',
                    'sem_id', 'academic_year')


#
#
#
#
#
admin.site.register(AccountCreated)
