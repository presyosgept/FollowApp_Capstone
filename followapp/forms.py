from multiselectfield import MultiSelectFormField
from django.forms.widgets import CheckboxSelectMultiple
from .models import Calendar, CounselorFeedback, Referral, SetScheduleCounselor, StudentAdditionalInformation, Subject, School, Department, Faculty, Counselor, SubjectOfferings, DegreeProgram, Student, Studentload
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

from django.utils import timezone

class CalendarForm(forms.ModelForm):
    pickedDate=forms.DateField(widget=forms.SelectDateWidget(), initial = timezone.now)
    class Meta:
        model = Calendar
        fields = ['pickedDate']
        


class FilterDateForm(forms.Form):
    pickedStartDate = forms.DateField(widget=forms.SelectDateWidget(), initial = timezone.now)
    pickedEndDate = forms.DateField(widget=forms.SelectDateWidget(), initial = timezone.now)
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





class AssignCounselorForm(forms.Form):
    qs = Faculty.objects.filter(role = 'Counselor')
    qs_code = []
    for obj in qs:
        name = obj.lastname + ', ' + obj.firstname
        qs_code.append([obj.faculty_id, name])
    faculty = forms.CharField(widget=forms.Select(choices=qs_code))


class EditDegreeProgramForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditDegreeProgramForm, self).__init__(*args, **kwargs)

    class Meta:
        model = DegreeProgram
        fields = ['program_name', 'school_code']


class EditSchoolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditSchoolForm, self).__init__(*args, **kwargs)
        self.fields['school_name'].disabled = True

    class Meta:
        model = School
        fields = ['school_code', 'school_name']


class EditDepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditDepartmentForm, self).__init__(*args, **kwargs)
        self.fields['department_code'].disabled = True

    class Meta:
        model = Department
        fields = ['department_code', 'department_name',
                  'school_code']


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


SEM_CHOICES = [
    ('--', '--'),
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('Summer', 'Summer'),
]


class CheckSemForm(forms.Form):
    sem = forms.CharField(widget=forms.Select(choices=SEM_CHOICES))
# Edit Data In admin


class StudentAdditionalInformationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentAdditionalInformationForm, self).__init__(*args, **kwargs)
        self.fields['student_number'].disabled = True
        self.fields['firstname'].disabled = True
        self.fields['lastname'].disabled = True
        self.fields['middlename'].disabled = True
        self.fields['student_email'].disabled = True

    class Meta:
        model = StudentAdditionalInformation
        fields = ['student_number', 'firstname', 'lastname', 'middlename',
                  'student_email', 'student_contact_number',
                  'mother_lastname', 'mother_firstname', 'mother_contact_number',
                  'father_lastname', 'father_firstname', 'father_contact_number',
                  'guardian_lastname', 'guardian_firstname', 'guardian_contact_number',
                  ]


class CounselorFeedbackForm(forms.ModelForm):
    feedback = forms.CharField(widget=forms.Textarea)
    remarks = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(CounselorFeedbackForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CounselorFeedback
        fields = '__all__'

class StudentSetSchedForm(forms.Form):
    reasons = forms.CharField(widget=forms.Textarea)


STATUS_CHOICES = (('--', '--'), ('all', 'All'), ('done', 'Done'),
                  ('pending', 'Pending'))


class FilterForm(forms.Form):
    filter_choice = forms.CharField(widget=forms.Select(
        choices=STATUS_CHOICES))


class ReferralForm(forms.Form):
    reasons = forms.CharField(widget=forms.Textarea)
    behavior_problem = MultiSelectFormField(
        widget=forms.CheckboxSelectMultiple, choices=Referral.BEHAVIOR_PROBLEM)
    student_number = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    subject_referred = forms.CharField()

TIME = (('--', '--'),
        ('07:00', '7:00 AM'), ('07:30', '7:30 AM'),
        ('08:00', '8:00 AM'), ('08:30', '8:30 AM'),
        ('09:00', '9:00 AM'), ('09:30', '9:30 AM'),
        ('10:00', '10:00 AM'), ('10:30', '10:30 AM'),
        ('11:00', '11:00 AM'), ('11:30', '11:30 AM'),
        ('12:00', '12:00 PM'), ('12:30', '12:30 PM'),
        ('13:00', '1:00 PM'), ('13:30', '1:30 PM'),
        ('14:00', '2:00 PM'), ('14:30', '2:30 PM'),
        ('15:00', '3:00 PM'), ('15:30', '3:30 PM'),
        ('16:00', '4:00 PM'), ('16:30', '4:30 PM'),
        ('17:00', '5:00 PM'), ('17:30', '5:30 PM'))


class SetScheduleCounselorForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.Select(
        choices=TIME))
    end_time = forms.TimeField(widget=forms.Select(
        choices=TIME))
    date = forms.DateField(widget=forms.SelectDateWidget(), initial = timezone.now)
    class Meta:
        model = SetScheduleCounselor
        fields = ['date', 'start_time', 'end_time']

        
# class ReferralForm(forms.ModelForm):
#     reasons = forms.CharField(widget=forms.Textarea)

#     def __init__(self, *args, **kwargs):
#         super(ReferralForm, self).__init__(*args, **kwargs)
#         self.fields['student_number'].disabled = True
#         self.fields['firstname'].disabled = True
#         self.fields['lastname'].disabled = True
#         self.fields['subject_referred'].disabled = True

#     behavior_problem = MultiSelectFormField(widget=forms.CheckboxSelectMultiple,
#                                             choices=Referral.BEHAVIOR_PROBLEM)

#     class Meta:
#         model = Referral
#         fields = ['student_number', 'firstname', 'lastname',
#                   'behavior_problem', 'subject_referred', 'reasons']


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



# class CalendarForm(forms.Form):
#     pickedDate = forms.DateField(widget=forms.SelectDateWidget())
# class FilterDateForm(forms.ModelForm):
#     class Meta:
#         model = FilterDate
#         fields = '__all__'


#         widgets = {
#             'pickedStartDate': DateInput(format='%m/%d/%Y'),
#             'pickedEndDate': DateInput(format='%m/%d/%Y')
#         }
