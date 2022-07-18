from multiselectfield import MultiSelectFormField
from django.forms.widgets import CheckboxSelectMultiple
from .models import Semester, Offerings, Subject, School, Department, Faculty, Counselor, SubjectOfferings, DegreeProgram, Student, Studentload
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class SearchForm(forms.Form):
    search = forms.CharField()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AccountsForm(forms.Form):
    password = forms.CharField()


class VerificationForm(forms.Form):
    code = forms.CharField()


class AccountCreatedForm(forms.Form):
    id_number = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

# Edit Data In admin


class EditDepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditDepartmentForm, self).__init__(*args, **kwargs)
        self.fields['department_code'].disabled = True

    class Meta:
        model = Department
        fields = ['department_code', 'department_name',
                  'school_code']


# class EditSubjectForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(EditSubjectForm, self).__init__(*args, **kwargs)
#         self.fields['subject_code'].disabled = True
#         self.fields['subject_title'].disabled = True

#     class Meta:
#         model = Subject
#         fields = ['subject_code', 'subject_title', 'units']


UNITS_CHOICES = [
    ('--', '--'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
]


class EditSubjectForm(forms.Form):
    units = forms.CharField(widget=forms.Select(choices=UNITS_CHOICES))
# Edit Data In admin


qs = Faculty.objects.all()
qs_code = []
for obj in qs:
    if obj.role == 'Counselor':
        name = obj.lastname + ',' + obj.firstname
        qs_code.append([obj.faculty_id, name])


class AssignCounselorForm(forms.Form):
    faculty = forms.CharField(widget=forms.Select(choices=qs_code))

# class SearchForm(forms.Form):
#     search = forms.CharField()


# class StudentInfoForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super(StudentInfoForm, self).__init__(*args, **kwargs)
#         self.fields['studnumber'].disabled = True
#         self.fields['firstname'].disabled = True
#         self.fields['lastname'].disabled = True
#         self.fields['program_code'].disabled = True
#         self.fields['year'].disabled = True
#         self.fields['student_email'].disabled = True

#     class Meta:
#         model = StudentInfo
#         fields = ['studnumber', 'firstname', 'lastname',  'degree_program',
#                   'year', 'student_email', 'student_contact_number',
#                   'mother_lastname', 'mother_firstname',
#                   'father_lastname', 'father_firstname',
#                   'guardian_lastname', 'guardian_firstname',
#                   'mother_contact_number',
#                   'father_contact_number',
#                   'guardian_contact_number',
#                   ]


# class OfferingForm(forms.ModelForm):
#     class Meta:
#         model = Offering
#         fields = '__all__'


# class CounselorFeedbackForm(forms.ModelForm):
#     feedback = forms.CharField(widget=forms.Textarea)
#     remarks = forms.CharField(widget=forms.Textarea)

#     def __init__(self, *args, **kwargs):
#         super(CounselorFeedbackForm, self).__init__(*args, **kwargs)

#     class Meta:
#         model = CounselorFeedback
#         fields = '__all__'
# # # class FeedbackForm(forms.Form):
# # #     feedback = forms.CharField(widget=forms.Textarea)


# class StudentSetSchedForm(forms.ModelForm):
#     reasons = forms.CharField(widget=forms.Textarea)

#     def __init__(self, *args, **kwargs):
#         super(StudentSetSchedForm, self).__init__(*args, **kwargs)
#         self.fields['studnumber'].disabled = True
#         self.fields['firstname'].disabled = True
#         self.fields['lastname'].disabled = True

#     class Meta:
#         model = StudentSetSched
#         fields = ['studnumber', 'firstname', 'lastname',  'reasons']


# STATUS_CHOICES = (('--', '--'), ('all', 'All'), ('done', 'Done'),
#                   ('pending', 'Pending'))


# class FilterForm(forms.Form):
#     filter_choice = forms.CharField(widget=forms.Select(
#         choices=STATUS_CHOICES))


# class TeachersReferralForm(forms.ModelForm):
#     reasons = forms.CharField(widget=forms.Textarea)

#     def __init__(self, *args, **kwargs):
#         super(TeachersReferralForm, self).__init__(*args, **kwargs)
#         self.fields['studnumber'].disabled = True
#         self.fields['firstname'].disabled = True
#         self.fields['lastname'].disabled = True
#         self.fields['subject_referred'].disabled = True

#     behavior_problem = MultiSelectFormField(widget=forms.CheckboxSelectMultiple,
#                                             choices=TeachersReferral.BEHAVIOR_PROBLEM)

#     class Meta:
#         model = TeachersReferral
#         fields = ['studnumber', 'firstname', 'lastname',
#                   'behavior_problem', 'subject_referred', 'reasons', 'feedback']


# class StudentsForm(forms.Form):
#     studnumber = forms.CharField()
#     firstname = forms.CharField()
#     lastname = forms.CharField()
#     email = forms.CharField()
#     course = forms.CharField()
#     year = forms.CharField()
#     role = forms.CharField()


# class SubjectOfferedForm(forms.Form):
#     offer_no = forms.CharField()
#     subject_no = forms.CharField()
#     subject_title = forms.CharField()
#     dayofsub = forms.CharField()
#     start_time = forms.TimeField()
#     end_time = forms.TimeField()
#     units = forms.CharField()


# class FacultyloadForm(forms.Form):
#     offer_no = forms.CharField()
#     employeeid = forms.CharField()


# class StudentsloadForm(forms.Form):
#     id = forms.CharField()
#     offer_no = forms.CharField()
#     studnumber = forms.CharField()


# class ProgramForm(forms.Form):
#     program = forms.CharField()


# class DeleteSchoolOfficeForm(forms.Form):
#     schoolform_code = forms.CharField()


# class AddSchoolOfficeForm(forms.Form):
#     school_code = forms.CharField()
#     school_office_name = forms.CharField()

# # class AddSchoolOfficeForm(forms.ModelForm):
# #     def __init__(self, *args, **kwargs):
# #         super(AddSchoolOfficeForm, self).__init__(*args, **kwargs)
# #         self.fields['school_id'].disabled = True

# #     class Meta:
# #         model = SchoolOffices
# #         fields = ['school_id', 'school_code',
# #                   'school_office_name']


# class DeleteDepartmentForm(forms.Form):
#     del_department_name_form = forms.CharField()


# class AddDepartmentForm(forms.Form):
#     department_name_form = forms.CharField()
#     # school_code_form = forms.CharField()
#     # def __init__(self, *args, **kwargs):
#     #     super(AddDepartmentForm, self).__init__(*args, **kwargs)
#     #     self.fields['school_code'].disabled = True

#     # class Meta:
#     #     model = Department
#     #     fields = ['department_id', 'department_name',
#     #               'school_code']


# class CounselorForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super(CounselorForm, self).__init__(*args, **kwargs)
#         self.fields['employee_id'].disabled = True
#         self.fields['firstname'].disabled = True
#         self.fields['lastname'].disabled = True
#     # program_designation = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
#     #                                                      queryset=DegreeProgram.objects.values_list('program_code'))
#     # program_designation = MultiSelectFormField(widget=forms.CheckboxSelectMultiple,
#     #                                            choices=Counselor.PROGRAM_DESIGNATION)

#     class Meta:
#         model = Counselor
#         fields = ['employee_id', 'firstname',
#                   'lastname', 'program_designation']


# class DateInput(forms.DateInput):
#     input_type = 'date'


# class CalendarForm(forms.ModelForm):
#     class Meta:
#         model = Calendar
#         fields = '__all__'

#         widgets = {
#             'pickedDate': DateInput(format='%m/%d/%Y'),
#         }


# class FilterDateForm(forms.ModelForm):
#     class Meta:
#         model = FilterDate
#         fields = '__all__'

#         widgets = {
#             'pickedStartDate': DateInput(format='%m/%d/%Y'),
#             'pickedEndDate': DateInput(format='%m/%d/%Y')
#         }


# TIME = (('--', '--'),
#         ('7:00', '7:00 A.M.'), ('7:30', '7:30 A.M.'),
#         ('8:00', '8:00 A.M.'), ('8:30', '8:30 A.M.'),
#         ('9:00', '9:00 A.M.'), ('9:30', '9:30 A.M.'),
#         ('10:00', '10:00 A.M.'), ('10:30', '10:30 A.M.'),
#         ('11:00', '11:00 A.M.'), ('11:30', '11:30 A.M.'),
#         ('12:00', '12:00 P.M.'), ('12:30', '12:30 P.M.'),
#         ('13:00', '1:00 P.M.'), ('13:30', '1:30 P.M.'),
#         ('14:00', '2:00 P.M.'), ('14:30', '2:30 P.M.'),
#         ('15:00', '3:00 P.M.'), ('15:30', '3:30 P.M.'),
#         ('16:00', '4:00 P.M.'), ('16:30', '4:30 P.M.'),
#         ('17:00', '5:00 P.M.'), ('17:30', '5:30 P.M.'))


# class SetScheduleCounselorForm(forms.ModelForm):
#     start_time = forms.CharField(widget=forms.Select(
#         choices=TIME))
#     end_time = forms.CharField(widget=forms.Select(
#         choices=TIME))

#     class Meta:
#         model = SetScheduleCounselor
#         fields = ['employee_id', 'date',
#                   'start_time', 'end_time']

#         widgets = {
#             'date': DateInput(format='%Y-%m-%d'),
#         }
