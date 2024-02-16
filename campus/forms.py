from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms.widgets import DateInput,CheckboxSelectMultiple
from django.http import request
# from bootstrap_datepicker_plus import DatePickerInput



class Student_SignUpForm(UserCreationForm):
    #image=forms.ImageField(required=False)
    name = forms.CharField(max_length=30, required=True, help_text='*required')
    phone_number = forms.CharField(max_length=10, min_length=10,required=True, help_text='*required')
    fathers_name = forms.CharField(max_length=30, required=True, help_text='*required')
    mothers_name = forms.CharField(max_length=30, required=True, help_text='*required')
    gender= forms.CharField(max_length=30, required=True, help_text='*required')
    place = forms.CharField(max_length=30, required=True, help_text='*required')
    branch = forms.CharField(max_length=30, required=True, help_text='*required')
    cgpa_Btech = forms.FloatField(max_value=10,min_value=0 ,required=True, help_text='*required')
    class_10_cgpa = forms.FloatField(max_value=10,min_value=0 ,required=True, help_text='*required')
    class_12_percentage = forms.IntegerField(max_value=100,min_value=0, required=True, help_text='*required')
    certifications_count = forms.IntegerField(max_value=100,min_value=0, required=True, help_text='*required')
    internship = forms.CharField(max_length=10, min_length=2,required=True, help_text='*required')
    languages = forms.CharField(max_length=10, min_length=3,required=True, help_text='*required')
    sop = forms.CharField(max_length=10, min_length=0,required=True, help_text='*required')
    #dob = forms.DateField(required=True)
    dob = forms.DateField(required=True, help_text='*format is YYYY-MM-DD', )
    # date = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    skills=forms.CharField(max_length=100, min_length=0,required=True, help_text='*required')
    hobbies=forms.CharField(max_length=100, min_length=0,required=True, help_text='*required')
    about=forms.CharField(max_length=100, min_length=0,required=True, help_text='*required')


    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User  
        fields = ( 'name','dob','phone_number','email','fathers_name','mothers_name','gender','place','branch','cgpa_Btech','class_10_cgpa','class_12_percentage','certifications_count','internship','languages','sop','skills','username','password1', 'password2', )
        widgets={
            'dob': DateInput()
            }



class dept_SignUpForm(UserCreationForm):
    fname = forms.CharField(max_length=30, required=True, help_text='*required')
    lname = forms.CharField(max_length=30, required=True, help_text='*required')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'fname', 'lname','email','password1', 'password2', )
        widgets={'dob':DateInput(attrs={'type':'date'})}


class UsdForm(forms.Form):
    sop = forms.CharField(max_length=500, initial="Enter ur sop",required=True)
    phone_number = forms.CharField(max_length=10,min_length=10,initial="enter ur phn num",required=True)

class dispstuForm(forms.ModelForm):
    class Meta:
        model=stu_details
        fields=('username','phone_number','fathers_name','mothers_name','gender','place','branch','cgpa_Btech','class_10_cgpa','class_12_percentage','certifications_count',\
               'internship','languages','sop','dob')


c_type = (
    ('product', 'product'),
    ('service', 'service'))


class company_SignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=30, required=True, help_text='*required')
    est_year=forms.CharField(max_length=4,required=True,help_text="*required")
    hr_name=forms.CharField(max_length=30, required=True, help_text='*required')
    hr_phn=forms.CharField(max_length=10, min_length=10,required=True, help_text='*required')
    headquaters=forms.CharField(max_length=30, required=True, help_text='*required')
    about=forms.CharField(max_length=1000, required=True, help_text='*required')
    type=forms.ChoiceField(required=True,choices=c_type)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'company_name', 'est_year','hr_name','hr_phn','headquaters','about','type','email','password1', 'password2', )


class ccdForm(forms.Form):
    hr_name = forms.CharField(max_length=30, required=True, help_text='*required')
    hr_phn = forms.CharField(max_length=10, min_length=10, required=True, help_text='*required')
    about=forms.CharField(max_length=1000, required=True, help_text='*required')


class jobposForm(forms.ModelForm):
    class Meta:
        model=job_pos
        fields=('company_name','username','job_id','designation' ,'salary'  ,'bond_years','information_technology','mech', 'civil','eee',  'ece', 'chemical' ,'cse')

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'desc', 'number_of_questions', 'time')

    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content', 'quiz')
        
# class DocumentForm(forms.Form):
#     docfile = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )
# class UploadForm(forms.Form):
#     file_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
class MyfileUploadForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # comapany_selected = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    files_data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

class studentCompanyApply(forms.Form):
    usn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
