from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django import forms
import random
done = (
    ('yes', 'yes'),
    ('no', 'no'),
)

# class Student_Details(models.Model):
#     branch_choices = (
#         ('it', 'information_technology'),
#         ('me', 'mech'),
#         ('ce', 'civil'),
#         ('eee', 'eee'),
#         ('ece', 'ece'),
#         ('ch', 'chemical'),
#         ('cse', 'cse'),
#     )
#     gender = (
#         ('male', 'male'),
#         ('female', 'female'),
#         ('others','others'))

#     username=models.CharField(max_length=9,blank=False,help_text="enter username ex:y16it***",default="y1")
#     name = models.CharField(max_length=30, blank=False, help_text='*required',default="full name")
#     image = models.ImageField(default='default.jpg', upload_to='profile_picsnew')
#     phone_number = models.CharField(max_length=10,help_text='*required')
#     fathers_name = models.CharField(max_length=30, blank=False, help_text='*required')
#     mothers_name = models.CharField(max_length=30, blank=False, help_text='*required')
#     gender=models.CharField(blank=False, choices=gender,max_length=10)
#     place = models.CharField(max_length=30, blank=False)
#     branch = models.CharField(blank=False, choices=branch_choices, max_length=10)
#     cgpa_Btech = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False,help_text='*required')
#     class_10_cgpa = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False,help_text='*required')
#     class_12_percentage = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False,help_text='*required')
#     certifications_count = models.IntegerField(blank=False)
#     internship = models.CharField(blank=False, choices=done,max_length=10)
#     languages = models.CharField(max_length=100, blank=False, help_text='*required')
#     sop = models.CharField(max_length=500, default="statement of purpose", help_text='*required')
#     dob = models.DateField(blank=True, help_text='*format is YYYY-MM-DD', )
#     email = models.EmailField(max_length=254, blank=False, help_text='Required. Inform a valid email address.',default="anudeep.insvirat@gmail.com")
#     skills=models.CharField(max_length=100, blank=False,default="java")
#     hobbies=models.CharField(max_length=100, blank=False,default="dance")
#     about=models.TextField(default="about ur self")
    
#     def __str__(self):
#        return self.username

class stu_details(models.Model):
    branch_choices = (
        ('it', 'information_technology'),
        ('me', 'mech'),
        ('ce', 'civil'),
        ('eee', 'eee'),
        ('ece', 'ece'),
        ('ch', 'chemical'),
        ('cse', 'cse'),
    )
    gender = (
        ('male', 'male'),
        ('female', 'female'),
        ('others','others'))

    username=models.CharField(max_length=10,blank=False, help_text="enter username ex:y16it***",default="y1")
    name = models.CharField(max_length=30, blank=False, help_text='*required',default="full name")
    # image = models.ImageField(default='default.jpg', upload_to='profile_picsnew')
    phone_number = models.CharField(max_length=10, help_text='*required')
    fathers_name = models.CharField(max_length=30, blank=False, help_text='*required')
    mothers_name = models.CharField(max_length=30, blank=False, help_text='*required')
    gender=models.CharField(blank=False, choices=gender,max_length=10)
    place = models.CharField(max_length=30, blank=False)
    branch = models.CharField(blank=False, choices=branch_choices, max_length=10)
    cgpa_Btech = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False,help_text='*required')
    class_10_cgpa = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False,help_text='*required')
    class_12_percentage = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False,help_text='*required')
    certifications_count = models.IntegerField(blank=False)
    internship = models.CharField(blank=False, choices=done,max_length=10)
    languages = models.CharField(max_length=100, blank=False, help_text='*required')
    sop = models.CharField(max_length=500, default="statement of purpose", help_text='*required')
    dob = models.DateField(blank=False, help_text='*format is YYYY-MM-DD',)
    email = models.EmailField(max_length=254, blank=False, help_text='Required. Inform a valid email address.',default="anudeep.insvirat@gmail.com")
    skills=models.CharField(max_length=100, blank=False,default="java")
    hobbies=models.CharField(max_length=100, blank=False,default="dance")
    about=models.TextField(default="about ur self")
    
    def __str__(self):
       return self.username

class dept_details(models.Model):
   
    username=models.CharField(max_length=9,blank=False,help_text="enter username ex:y16it***",default="y1")
    name = models.CharField(max_length=30, blank=False, help_text='*required',default="full name")
    dob = models.DateField(blank=False, help_text='*format is YYYY-MM-DD', )
    email = models.EmailField(max_length=254, blank=False, help_text='Required. Inform a valid email address.',default="anudeep.insvirat@gmail.com")

    def __str__(self):
       return self.username



class comp_details(models.Model):
    username=models.CharField(max_length=30,blank=False , help_text='*required')
    company_name = models.CharField(max_length=30, blank=False, help_text='*required')
    est_year = models.CharField(max_length=4, blank=False, help_text="*required")
    hr_name = models.CharField(max_length=30, blank=False, help_text='*required')
    hr_phn = models.CharField(max_length=10,validators=[MinValueValidator(10),MaxValueValidator(10)], blank=False, help_text='*required')
    headquaters = models.CharField(max_length=30,blank=False, help_text='*required')
    about = models.CharField(max_length=1000, blank=False, help_text='*required')
    type = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254,blank=False, help_text='Required. Inform a valid email address.')

    def __str__(self):
        return self.username

class job_pos(models.Model):
    job_id=models.CharField(max_length=30, blank=False, help_text='*required',unique=True)
    username = models.CharField(max_length=30, blank=False, help_text='*required')
    company_name = models.CharField(max_length=30, blank=False, help_text='*required')
    designation = models.CharField(max_length=30, blank=False, help_text='*required')
    salary=models.IntegerField( blank=False, help_text='*required')
    bond_years=models.IntegerField( blank=False, help_text='*required')
    information_technology= models.CharField(blank=False, choices=done, max_length=10)
    mech= models.CharField(blank=False, choices=done, max_length=10)
    civil= models.CharField(blank=False, choices=done, max_length=10)
    eee = models.CharField(blank=False, choices=done, max_length=10)
    ece= models.CharField(blank=False, choices=done, max_length=10)
    chemical= models.CharField(blank=False, choices=done, max_length=10)
    cse= models.CharField(blank=False, choices=done, max_length=10)

    def __str__(self):
        return self.job_id


class applied_jobs(models.Model):
    company_id = models.CharField(max_length=30, blank=False, help_text='*required' ,default="company id")
    job_id = models.CharField(max_length=30, blank=False, help_text='*required',default="job id")
    student_id= models.CharField(max_length=9, blank=False, help_text="enter username ex:y16it***", default="y1")

    def __str__(self):
        return self.job_id


# User.student = property(lambda p: stu_details.objects.get_or_create(user=p)[0])


#Quiz
class Quiz(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="1")
    
    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()
    
class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.answer_set.all()
    
    
class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}, correct: {self.correct}"
    
class Marks_Of_User(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.quiz)

class Offer_letter(models.Model):
    ids = models.AutoField(primary_key=True)
    # usn = models.ForeignKey(stu_details, on_delete = models.CASCADE)
    usn = models.CharField(max_length=255)
    # company_selected = models.CharField(max_length=255)
    my_file = models.FileField(upload_to='')
    
    def __str__(self):
        return self.usn
    
class Java(models.Model):
    f_name=models.CharField(max_length=255)
    myfiles=models.FileField(upload_to="")
    

    def __str__(self):
        return self.f_name

class C(models.Model):
    f_name=models.CharField(max_length=255)
    myfiles=models.FileField(upload_to="")

    def __str__(self):
        return self.f_name

        
class DBMS(models.Model):
    f_name=models.CharField(max_length=255)
    myfiles=models.FileField(upload_to="")

    def __str__(self):
        return self.f_name


class CN(models.Model):
    f_name=models.CharField(max_length=255)
    myfiles=models.FileField(upload_to="")

    def __str__(self):
        return self.f_name

class OS(models.Model):
    f_name=models.CharField(max_length=255)
    myfiles=models.FileField(upload_to="")

    def __str__(self):
        return self.f_name

class ALGO(models.Model):
    f_name=models.CharField(max_length=255)
    myfiles=models.FileField(upload_to="")

    def __str__(self):
        return self.f_name

class OTHER(models.Model):
    f_name=models.CharField(max_length=255)
    myfiles=models.FileField(upload_to="")
    batch_name=models.CharField(max_length=255)

    def __str__(self):
        return self.f_name+''+self. batch_name


class DS(models.Model):
    f_name=models.CharField(max_length=255)
    myfiles=models.FileField(upload_to="")
    batch_name=models.CharField(max_length=255)

    def __str__(self):
        return self.f_name+''+self. batch_name

class BroadCast_Email(models.Model):
    subject = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    message = RichTextUploadingField()

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = "BroadCast Email to all Member"
        verbose_name_plural = "BroadCast Email"

class studentCompanyApplied(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length = 255)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username