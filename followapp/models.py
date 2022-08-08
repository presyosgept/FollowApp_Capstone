from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField
from viewflow.fields import CompositeKey
from compositefk.fields import CompositeForeignKey, LocalFieldValue


class Referral(models.Model):
    student_number = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220, blank=True, null=True)
    lastname = models.CharField(max_length=220, blank=True, null=True)
    middlename = models.CharField(max_length=220, blank=True, null=True)
    degree_program = models.CharField(max_length=220, blank=True, null=True)
    subject_referred = ArrayField(
        ArrayField(
            models.CharField(max_length=225)
        ), blank=True, null=True
    )
    reasons = ArrayField(
        ArrayField(
            models.CharField(max_length=10000)
        ), blank=True, null=True
    )
    counselor_id = models.CharField(max_length=220, blank=True, null=True)
    faculty_id = ArrayField(
        ArrayField(
            models.CharField(max_length=225, blank=True, null=True)
        ), blank=True, null=True
    )
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=220, default='pending')
    BEHAVIOR_PROBLEM = (('CHEATING', 'CHEATING'),
                        ('TARDINESS', 'TARDINESS'), ('DISRESPECTFUL', 'DISRESPECTFUL'),
                        ('BAD ATTITUDE', 'BAD ATTITUDE'), ('OTHERS', 'OTHERS'))
    behavior_problem = MultiSelectField(
        max_length=220, choices=BEHAVIOR_PROBLEM, blank=True, null=True)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    choice = models.CharField(max_length=220, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Referral"


class Subject(models.Model):
    subject_code = models.CharField(max_length=225, primary_key=True)
    subject_title = models.CharField(max_length=220)
    units = models.CharField(max_length=220)

    class Meta:
        verbose_name_plural = "Subject"


class School(models.Model):
    school_code = models.CharField(max_length=220)
    school_name = models.CharField(max_length=220)

    class Meta:
        verbose_name_plural = "School"

    def __str__(self):
        return self.school_code


class Department(models.Model):
    department_code = models.CharField(max_length=25, primary_key=True)
    department_name = models.CharField(max_length=220)
    school_code = models.ForeignKey(
        School, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Department"

    def __str__(self):
        return self.school_code


class Faculty(models.Model):
    faculty_id = models.CharField(max_length=15, primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    middlename = models.CharField(max_length=220)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=220)
    department_code = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Faculty"


class Counselor(models.Model):
    counselor_id = models.CharField(max_length=220, primary_key=True)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)

    class Meta:
        verbose_name_plural = "Counselor"


class SubjectOfferings(models.Model):
    class Meta:
        verbose_name_plural = "SubjectOfferings"
        constraints = [
            models.UniqueConstraint(
                fields=['offer_no', 'sem_id'], name='offer_no_and_sem_id_uniq_SubjectOfferings')
        ]
    offer_no = models.CharField(max_length=220,)
    subject_code = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True, blank=True)
    subject_title = models.CharField(max_length=220)
    school_days = models.CharField(max_length=220)
    school_time = models.CharField(max_length=220)
    sem_id = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=225)
    department_code = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)
    faculty_id = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, blank=True)


class DegreeProgram(models.Model):
    program_code = models.CharField(max_length=220, primary_key=True)
    program_name = models.CharField(max_length=220)
    school_code = models.ForeignKey(
        School, on_delete=models.CASCADE, null=True, blank=True)
    faculty_id = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "DegreeProgram"


class Student(models.Model):
    student_number = models.CharField(max_length=15, primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    middlename = models.CharField(max_length=220)
    school_name = models.ForeignKey(
        School, on_delete=models.CASCADE, null=True, blank=True)
    department_code = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)
    program_code = models.ForeignKey(
        DegreeProgram, on_delete=models.CASCADE, null=True, blank=True)
    academic_year = models.CharField(max_length=225)
    sem_id = models.CharField(max_length=220)
    student_email = models.EmailField(max_length=254)
    role = models.CharField(max_length=220)

    class Meta:
        verbose_name_plural = "Student"


class Studentload(models.Model):
    class Meta:
        verbose_name_plural = "Studentload"
        constraints = [
            models.UniqueConstraint(
                fields=['student_number', 'offer_no'], name='student_number_and_offer_no_uniq_Studentload')
        ]
    student_number = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True)
    offer_no = models.ForeignKey(
        SubjectOfferings, on_delete=models.CASCADE, null=True, blank=True)
    sem_id = models.CharField(max_length=220)
    academic_year = models.CharField(max_length=225)

#
#
#
#
# own table


class AccountCreated(models.Model):
    id_number = models.CharField(max_length=15, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=220)

    class Meta:
        verbose_name_plural = "AccountCreated"


class StudentAdditionalInformation(models.Model):
    student_number = models.CharField(max_length=15, primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    middlename = models.CharField(max_length=220)
    student_email = models.EmailField(max_length=254)
    student_contact_number = models.CharField(max_length=220)
    mother_lastname = models.CharField(max_length=220)
    mother_firstname = models.CharField(max_length=220)
    mother_contact_number = models.CharField(max_length=220)
    father_lastname = models.CharField(max_length=220)
    father_firstname = models.CharField(max_length=220)
    father_contact_number = models.CharField(max_length=220)
    guardian_lastname = models.CharField(max_length=220)
    guardian_firstname = models.CharField(max_length=220)
    guardian_contact_number = models.CharField(max_length=220)
    status = models.CharField(max_length=254, default='undone')

    class Meta:
        verbose_name_plural = "StudentAdditionalInformation"


class SetScheduleCounselor(models.Model):
    faculty_id = models.CharField(max_length=220)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    choice = models.CharField(max_length=220)

    class Meta:
        verbose_name_plural = "SetScheduleCounselor"


class Notification(models.Model):
    AUTOMATIC_REFERRAL = 'automatic_referral'
    MANUAL_REFERRAL = 'manual_referral'
    APPOINTMENT = 'appointment'

    CHOICES = (
        (AUTOMATIC_REFERRAL, 'automatic_referral'),
        (MANUAL_REFERRAL, 'manual_referral'),
        (APPOINTMENT, 'appointment')
    )

    to_user = models.CharField(max_length=220)
    notification_type = models.CharField(max_length=100, choices=CHOICES)
    is_read_student = models.BooleanField(default=False)
    is_read_counselor = models.BooleanField(default=False)
    extra_id = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=220)
    schedDay = models.DateTimeField()
    schedStartTime = models.TimeField()
    schedEndTime = models.TimeField()

    class Meta:
        verbose_name_plural = "Notification"


class NotificationFeedback(models.Model):
    FEEDBACK_TEACHER = 'feedback_teacher'
    FEEDBACK_STUDENT = 'feedback_student'

    CHOICES = (
        (FEEDBACK_TEACHER, 'feedback_teacher'),
        (FEEDBACK_STUDENT, 'feedback_student')
    )

    to_user = models.CharField(max_length=220)
    notification_type = models.CharField(max_length=100, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField()
    referral_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=220)

    class Meta:
        verbose_name_plural = "NotificationFeedback"


class CounselorFeedback(models.Model):
    feedback = models.CharField(max_length=10000)
    remarks = models.CharField(max_length=10000)

    class Meta:
        verbose_name_plural = "CounselorFeedback"


class Calendar(models.Model):
    pickedDate = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Calendar"

# class AccountsApi(models.Model):
#     id_number = models.CharField(max_length=15, primary_key=True)
#     email = models.CharField(max_length=220)
#     code = models.CharField(max_length=220)

#     class Meta:
#         verbose_name_plural = "AccountsApi"


# class Offering(models.Model):
#     SEMESTER = (('1ST SEM', '1ST SEM'),
#                 ('2ND SEM', '2ND SEM'),
#                 ('SUMMER', 'SUMMER'))
#     semester = models.CharField(
#         max_length=220, choices=SEMESTER, default='1ST SEM', null=False, blank=False)
#     SCHOOL_YEAR = (('2019-2020', '2019-2020'),
#                    ('2020-2021', '2020-2021'),
#                    ('2021-2022', '2021-2022'))
#     school_year = models.CharField(
#         max_length=220, choices=SCHOOL_YEAR, default='2021-2022',  null=False, blank=False)
#     qs = NewDepartment.objects.all()
#     qs_code = []
#     for obj in qs:
#         qs_code.append([obj.department_name, obj.department_name])
#     depa_choice = models.CharField(default='---',
#                                    max_length=220, choices=qs_code, null=False, blank=False)

#     class Meta:
#         verbose_name_plural = "Offering"


# class TeachersReferral(models.Model):
#     student_number = models.CharField(max_length=220)
#     firstname = models.CharField(max_length=220)
#     lastname = models.CharField(max_length=220)
#     program_code = models.CharField(max_length=220)
#     subject_referred = models.CharField(max_length=220)
#     reasons = models.CharField(max_length=10000)
#     counselor = models.CharField(max_length=220)
#     employeeid = models.CharField(max_length=220)
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     status = models.CharField(
#         max_length=220, blank=True, null=True, default='pending')
#     BEHAVIOR_PROBLEM = (('CHEATING', 'CHEATING'),
#                         ('TARDINESS', 'TARDINESS'), ('DISRESPECTFUL', 'DISRESPECTFUL'),
#                         ('BAD ATTITUDE', 'BAD ATTITUDE'), ('OTHERS', 'OTHERS'))
#     behavior_problem = MultiSelectField(
#         max_length=220, choices=BEHAVIOR_PROBLEM)
#     feedback = models.CharField(max_length=10000)
#     choice = models.CharField(max_length=220)

#     class Meta:
#         verbose_name_plural = "TeachersReferral"


# class StudentSetSched(models.Model):
#     studnumber = models.CharField(max_length=220)
#     firstname = models.CharField(max_length=220)
#     lastname = models.CharField(max_length=220)
#     degree_program = models.CharField(max_length=220)
#     reasons = models.CharField(max_length=10000)
#     counselor = models.CharField(max_length=220)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     date = models.DateField()

#     class Meta:
#         verbose_name_plural = "StudentSetSched"


# class CounselorFeedback(models.Model):
#     feedback = models.CharField(max_length=10000)
#     remarks = models.CharField(max_length=10000)

#     class Meta:
#         verbose_name_plural = "CounselorFeedback"


# class FilterDate(models.Model):
#     pickedStartDate = models.DateField()
#     pickedEndDate = models.DateField()

#     class Meta:
#         verbose_name_plural = "FilterDate"


class NewTime(models.Model):
    time_id = models.CharField(max_length=220, primary_key=True)
    time1 = models.TimeField()
    time2 = models.TimeField()

    class Meta:
        verbose_name_plural = "NewTime"
