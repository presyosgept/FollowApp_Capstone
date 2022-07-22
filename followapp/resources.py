from import_export import resources
from .models import Semester, Subject, School, Department, Faculty, Counselor, SubjectOfferings, DegreeProgram, Student, Studentload


class SemesterResource(resources.ModelResource):
    class Meta:
        model = Semester


class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject


class SchoolResource(resources.ModelResource):
    class Meta:
        model = School


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department


class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty


class CounselorResource(resources.ModelResource):
    class Meta:
        model = Counselor


class SubjectOfferingsResource(resources.ModelResource):
    class Meta:
        model = SubjectOfferings


class DegreeProgramResource(resources.ModelResource):
    class Meta:
        model = DegreeProgram


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class StudentloadResource(resources.ModelResource):
    class Meta:
        model = Studentload
