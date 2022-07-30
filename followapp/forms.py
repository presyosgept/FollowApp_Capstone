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


qs = Faculty.objects.all()
qs_code = []
for obj in qs:
    if obj.role == 'Counselor':
        name = obj.lastname + ', ' + obj.firstname
        qs_code.append([obj.faculty_id, name])


class AssignCounselorForm(forms.Form):
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


SEM_CHOICES = [
    ('--', '--'),
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('Summer', 'Summer'),
]


class CheckSemForm(forms.Form):
    sem = forms.CharField(widget=forms.Select(choices=SEM_CHOICES))
# Edit Data In admin




# class SearchForm(forms.Form):
#     search = forms.CharField()


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
# class OfferingForm(forms.ModelForm):
#     class Meta:
#         model = Offering
#         fields = '__all__'


# # class FeedbackForm(forms.Form):
# #     feedback = forms.CharField(widget=forms.Textarea)


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


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['pickedDate']
        widgets = {
            'pickedDate': forms.SelectDateWidget()
        }

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
TIME = (('--', '--'),
        ('07:00 AM', '7:00 AM'), ('07:30 AM', '7:30 AM'),
        ('08:00 AM', '8:00 AM'), ('08:30 AM', '8:30 AM'),
        ('09:00 AM', '9:00 AM'), ('09:30 AM', '9:30 AM'),
        ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'),
        ('11:00 AM', '11:00 AM'), ('11:3 AM0', '11:30 AM'),
        ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'),
        ('01:00 PM', '1:00 PM'), ('01:30 PM', '1:30 PM'),
        ('02:00 PM', '2:00 PM'), ('02:30 PM', '2:30 PM'),
        ('03:00 PM', '3:00 PM'), ('03:30 PM', '3:30 PM'),
        ('04:00 PM', '4:00 PM'), ('04:30 PM', '4:30 PM'),
        ('05:00 PM', '5:00 PM'), ('05:30 PM', '5:30 PM'))


class SetScheduleCounselorForm(forms.ModelForm):
    start_time = forms.CharField(widget=forms.Select(
        choices=TIME))
    end_time = forms.CharField(widget=forms.Select(
        choices=TIME))

    class Meta:
        model = SetScheduleCounselor
        fields = ['faculty_id', 'date',
                  'start_time', 'end_time']

        widgets = {
            'date': DateInput(format='%Y-%m-%d'),
        }
