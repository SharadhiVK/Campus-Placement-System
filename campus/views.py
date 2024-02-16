from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from campus.models import *
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template import loader
#import pdfkit
import io
from django.core.files.storage import FileSystemStorage


#config = pdfkit.configuration(wkhtmltopdf="D:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

# Create your views here
def  student_login(request):
    
    print("##############",request.user.is_authenticated)
    if request.user.is_authenticated and request.user.groups.filter(name='student').exists():
        return render(request,'campus/stulog.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("form valie", request.user.groups.filter(name='student').exists())
            return render(request, 'campus/stulog.html', {'form': form})
            # if request.user.groups.filter(name='student').exists():
            #  return render(request, 'campus/stulog.html', {'form': form})
            # else:
            #     logout(request)
            #     return render(request, 'campus/student_login.html', {'form': form})
        else:
            return render(request, 'campus/student_login.html', {'form': form})


    else:
        form = AuthenticationForm()
        return render(request, 'campus/student_login.html', {'form': form})

def  dept_login(request):
    if request.user.is_authenticated and request.user.groups.filter(name='department').exists():
        return render(request,'campus/deptMain.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.groups.filter(name='department').exists():
             return render(request, 'campus/deptMain.html', {'form': form})
            else:
                logout(request)
                return render(request, 'campus/dept_login.html', {'form': form})
        else:
            return render(request, 'campus/dept_login.html', {'form': form})


    else:
        form = AuthenticationForm()
        return render(request, 'campus/dept_login.html', {'form': form})

def  home(request):
    return render(request,'campus/home.html')

def pagelogout(request):
        logout(request)

        return redirect('http://127.0.0.1:8000/')


def student_register(request):
    if request.method == 'POST':
        form = Student_SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            s=stu_details()
            s.username=request.POST.get('username')
            # a.first_name = request.POST.get('first_name')
            # a.last_name = request.POST.get('last_name')
            s.name = request.POST.get('name')
            s.phone_number = request.POST.get('phone_number')
            s.fathers_name = request.POST.get('fathers_name')
            s.mothers_name = request.POST.get('mothers_name')
            s.gender = request.POST.get('gender')
            s.place = request.POST.get('place')
            s.branch = request.POST.get('branch')
            s.cgpa_Btech = request.POST.get('cgpa_Btech')
            s.class_10_cgpa = request.POST.get('class_10_cgpa')
            s.class_12_percentage = request.POST.get('class_12_percentage')
            s.certifications_count = request.POST.get('certifications_count')
            s.internship = request.POST.get('internship')
            s.languages = request.POST.get('languages')
            s.sop = request.POST.get('sop')
            s.dob = request.POST.get('dob')
            s.email = request.POST.get('email')
            s.skills=request.POST.get('skills')
            s.hobbies=request.POST.get('hobbies')
            s.about=request.POST.get('about')

            
            s.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/student_login/')

        else:
            return render(request, 'campus/register.html', {'form': form})
    else:
        form = Student_SignUpForm()
        return render(request, 'campus/register.html', {'form': form})

def myresume(request):
    return render(request,'campus/resume/myresume.html')

def displayResume(request):
    stu = request.user.username
    user_profile = stu_details.objects.filter(username=stu)
    return render(request,'campus/resume/resume.html',{'user_profile':user_profile})

# def resume(request):
    
#     stu = request.user.username
#     user_profile = stu_details.objects.filter(username=stu)
#     template = loader.get_template('campus/resume/resume.html')
#     html = template.render({'user_profile':user_profile})
#     option = {
#         'page-size':'Letter',
#         'encoding':'UTF-8'
#     }

#     pdf = pdfkit.from_string(html,False,option,configuration=config)
#     response = HttpResponse(pdf,content_type = 'application/pdf')
#     response['Content-Disposition'] = 'attachment'
#     return response
#     # return render(request,'campus/stulog.html',{{'user_profile':user_profile}})


def dept_register(request):
    if request.method == 'POST':
        form = dept_SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='department')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/dept/dept_login/')

        else:
            return render(request, 'campus/register2.html', {'form': form})
    else:
        form =dept_SignUpForm()
        return render(request, 'campus/register2.html', {'form': form})
#@login_required
#@user_passes_test(lambda u: u.groups.filter(name='Student').count() == 1)
# def usd(request):
#  if  request.user.is_authenticated and request.user.groups.filter(name='student').exists():
#     if request.method == "POST":
#             form=UsdForm(request.POST)
#             if form.is_valid():
#                 stu = request.user.username
#                 post = stu_details.objects.filter(username=stu)
#                 x= request.POST.get('sop')
#                 y=request.POST.get('phone_number')
#                 db=request.POST.get('dob')
#                 e=request.POST.get('email')
#                 l=request.POST.get('languages') 
#                 cc=request.POST.get('certifications_count')
#                 i=request.POST.get('internship')
#                 c12=request.POST.get('class_12_percentage')
#                 c10=request.POST.get('class_10_cgpa')
#                 b=request.POST.get('branch')
#                 cb=request.POST.get('cgpa_Btech')
#                 p=request.POST.get('place')
#                 g=request.POST.get('gender')
#                 fn=request.POST.get('fathers_name')
#                 mn=request.POST.get('mothers_name')
#                 name=request.POST.get('name')

#                 j=post[0]
#                 j.sop =x
#                 j.phone_number = y
#                 j.dob="2022-09-9"
#                 j.email=e
#                 j.languages=l
#                 j.certifications_count=cc
#                 j.internship=i
#                 j.class_12_percentage=c12
#                 j.class_10_cgpa=c10
#                 j.branch=b
#                 j.cgpa_Btech=cb
#                 j.place=p
#                 j.gender=g
#                 j.fathers_name=fn
#                 j.mothers_name=mn
#                 j.name=name
#                 j.save()
#                 return render(request, 'campus/stulog.html')

#     else:
#         stu = request.user.username
#         post = stu_details.objects.filter(username=stu)
#         if len(post) > 0:
#             form=UsdForm()
#             phone_number = post[0].phone_number
            
#             db=post[0].dob
#             e=post[0].email
#             l=post[0].languages 
#             cc=post[0].certifications_count
#             i=post[0].internship
#             c12=post[0].class_12_percentage
#             c10=post[0].class_10_cgpa
#             b=post[0].branch
#             cb=post[0].cgpa_Btech
#             p=post[0].place
#             g=post[0].gender
#             fn=post[0].fathers_name
#             mn=post[0].mothers_name
#             name=post[0].name
#             data={'form': form,'x':phone_number,'y':db,'db': db,"e":e,"l":l,"cc":cc,"i":i,"c12":c12,"c10":c10,"b":b,"cb":cb,"p":p,"g":g,"fn":fn,"mn":mn,"name":name}
#             return render(request, 'campus/usd.html',context=data)
#         else:
#            return HttpResponse("<h1>u r not logged in</h1>")
#  else:
#      return HttpResponse("<h1>u r not logged in</h1>")

def usd(request):
#  print("request",and request.user.groups.filter(name='student').exists())
 if  request.user.is_authenticated :
    if request.method == "POST":
            form=UsdForm(request.POST)
            if form.is_valid():
                stu = request.user.username
                print("request post", request.POST)
                post = stu_details.objects.filter(username=stu)
                x= request.POST.get('sop')
                y=request.POST.get('phone_number')
                db=request.POST.get('dob')
                e=request.POST.get('email')
                l=request.POST.get('languages') 
                cc=request.POST.get('certifications_count')
                i=request.POST.get('internship')
                c12=request.POST.get('class_12_percentage')
                c10=request.POST.get('class_10_cgpa')
                b=request.POST.get('branch')
                cb=request.POST.get('cgpa_Btech')
                p=request.POST.get('place')
                g=request.POST.get('gender')
                fn=request.POST.get('fathers_name')
                mn=request.POST.get('mothers_name')
                name=request.POST.get('name')

                j=post[0]
                j.sop =x
                j.phone_number = y
                j.dob="2022-09-9"
                j.email=e
                j.languages=l
                j.certifications_count=cc
                j.internship=i
                j.class_12_percentage=c12
                j.class_10_cgpa=c10
                j.branch=b
                j.cgpa_Btech=cb
                j.place=p
                j.gender=g
                j.fathers_name=fn
                j.mothers_name=mn
                j.name=name
                j.save()
            return render(request, 'campus/stulog.html')

    else:
        stu = request.user.username
        print("uername", request.user.username)
         
        post = stu_details.objects.filter(username=stu)
        print("stud available", post)
        if len(post) > 0:
            form=UsdForm()
             
            phone_number = post[0].phone_number
            
            db=post[0].dob
            e=post[0].email
            l=post[0].languages 
            cc=post[0].certifications_count
            i=post[0].internship
            c12=post[0].class_12_percentage
            c10=post[0].class_10_cgpa
            b=post[0].branch
            cb=post[0].cgpa_Btech
            p=post[0].place
            g=post[0].gender
            fn=post[0].fathers_name
            mn=post[0].mothers_name
            name=post[0].name
            data={'form': form,'x':phone_number,'y':db,'db': db,"e":e,"l":l,"cc":cc,"i":i,"c12":c12,"c10":c10,"b":b,"cb":cb,"p":p,"g":g,"fn":fn,"mn":mn,"name":name}
            return render(request, 'campus/usd.html',context=data)
        else:
           return HttpResponse("<h1>u r not logged in</h1>")
 else:
     return HttpResponse("<h1>u r not logged in</h1>")

@login_required
def dispstu(request):
        stu = request.user.username
        post = stu_details.objects.filter(username=stu)
        if len(post) > 0:
            print("phone nu",post[0])
            return render(request, 'campus/dispstu.html', context= {'post':post[0]})
        else:
            return HttpResponse("<h1>u r not logged in</h1>")


def company_register(request):
    if request.method == 'POST':
        form = company_SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='company')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            a=comp_details()
            a.username=request.POST.get('username')
            a.company_name=request.POST.get('company_name')
            a.email=request.POST.get('email')
            a.est_year=request.POST.get('est_year')
            a.type=request.POST.get('type')
            a.about=request.POST.get('about')
            a.hr_name=request.POST.get('hr_name')
            a.hr_phn=request.POST.get('hr_phn')
            a.headquaters=request.POST.get('headquaters')
            a.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/company/company_login')
        else:
            return render(request, 'campus/register1.html', {'form': form})

    else:
        form =company_SignUpForm()
        return render(request, 'campus/register1.html', {'form': form})



def  company_login(request):
    if request.user.is_authenticated and request.user.groups.filter(name='company').exists():
        return render(request,'campus/comlog.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.groups.filter(name='company').exists():
             return render(request, 'campus/comlog.html', {'form': form})
            else:
                logout(request)
                return render(request, 'campus/company_login.html', {'form': form})
        else:
            return render(request, 'campus/company_login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'campus/company_login.html', {'form': form})




def ccd(request):
 if  request.user.is_authenticated and request.user.groups.filter(name='company').exists():
    if request.method == "POST":
            form=ccdForm(request.POST)
            if form.is_valid():
                stu = request.user.username
                post = comp_details.objects.filter(username=stu)
                x= request.POST.get('hr_name')
                y=request.POST.get('hr_phn')
                z=request.POST.get('about')
                j=post[0]
                j.hr_name =x
                j.hr_phn = y
                j.about=z
                j.save()
                return render(request, 'campus/comlog.html')

    else:
        stu = request.user.username
        post = comp_details.objects.filter(username=stu)
        x = post[0].hr_name
        x=str(x)
        y = post[0].hr_phn
        z=post[0].about
        form=ccdForm()
        return render(request, 'campus/ccd.html', {'form': form,'x':x,'y':y,'z':z})
 else:
     return HttpResponse("<h1>u r not logged in</h1>")





def contact(request):
    return render(request,'campus/contact.html')

def about(request):
    return render(request,'campus/about.html')


# def password_reset_request(request):
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "campus/password/password_reset_email.txt"
# 					c = {
# 					"email":user.email,
# 					'domain':'127.0.0.1:8000',
# 					'site_name': 'Website',
# 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 					"user": user,
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:
# 						return HttpResponse('Invalid header found.')
# 					return redirect ("/password_reset/done/")
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="campus/password/password_reset.html", context={"password_reset_form":password_reset_form})
# 	# if request.method == "POST":
	# 	password_reset_form = PasswordResetForm(request.POST)
	# 	if password_reset_form.is_valid():
	# 		data = password_reset_form.cleaned_data['email']
	# 		associated_users = User.objects.filter(Q(email=data))
	# 		if associated_users.exists():
	# 			for user in associated_users:
	# 				subject = "Password Reset Requested"
	# 				email_template_name = "campus/password/password_reset_email.txt"
	# 				c = {
	# 				"email":user.email,
	# 				'domain':'127.0.0.1:8000',
	# 				'site_name': 'Website',
	# 				"uid": urlsafe_base64_encode(force_bytes(user.pk)),
	# 				'token': default_token_generator.make_token(user),
	# 				'protocol': 'http',
	# 				}
	# 				email = render_to_string(email_template_name, c)
	# 				try:
	# 					send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
	# 				except BadHeaderError:

	# 					return HttpResponse('Invalid header found.')
						
	# 				messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
	# 				return redirect ("campus:homepage")
	# password_reset_form = PasswordResetForm()
	# return render(request=request, template_name="campus/password/password_reset.html", context={"password_reset_form":password_reset_form})\


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "campus/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website Name',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'https',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'shivaninaik20604@protonmail.com', [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ('/')
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="campus/password/password_reset.html", context={"password_reset_form":password_reset_form})


# def resume(request):
#     return render(request,'campus/resume.html')



def placementPrep(request):
    return render(request,'campus/placementPrep.html')

def quizindex(request):
    quiz = Quiz.objects.all()
    para = {'quiz' : quiz}
    return render(request, "campus/quizes/quizbase.html", para)

@login_required(login_url = '/student/student_login')
def quiz(request,myid):
    quiz = Quiz.objects.get(id=myid)
    return render(request, "campus/quizes/quiz.html", {'quiz':quiz})

def quiz_data_view(request, myid):
    quiz = Quiz.objects.get(id=myid)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.content)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, myid):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(content=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(id=myid)

        score = 0
        marks = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.content)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.content:
                        if a.correct:
                            score += 1
                            correct_answer = a.content
                    else:
                        if a.correct:
                            correct_answer = a.content

                marks.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                marks.append({str(q): 'not answered'})
     
        Marks_Of_User.objects.create(quiz=quiz, user=user, score=score)
        
        return JsonResponse({'passed': True, 'score': score, 'marks': marks})



def add_quiz(request):
    if request.method=="POST":
        form = QuizForm(data=request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            obj = form.instance
            return render(request, "campus/quizes/add_quiz.html", {'obj':obj})
    else:
        form=QuizForm()
    return render(request, "campus/quizes/add_quiz.html", {'form':form})

def add_question(request):
    questions = Question.objects.all()
    questions = Question.objects.filter().order_by('-id')
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "campus/quizes/add_question.html")
    else:
        form=QuestionForm()
    return render(request, "campus/quizes/add_question.html", {'form':form, 'questions':questions})

def delete_question(request, myid):
    question = Question.objects.get(id=myid)
    if request.method == "POST":
        question.delete()
        return redirect('/add_question')
    return render(request, "campus/quizes/delete_question.html", {'question':question})


def add_options(request, myid):
    question = Question.objects.get(id=myid)
    QuestionFormSet = inlineformset_factory(Question, Answer, fields=('content','correct', 'question'), extra=4)
    if request.method=="POST":
        formset = QuestionFormSet(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            alert = True
            return render(request, "campus/quizes/add_options.html", {'alert':alert})
    else:
        formset=QuestionFormSet(instance=question)
    return render(request, "campus/quizes/add_options.html", {'formset':formset, 'question':question})

def results(request):
    marks = Marks_Of_User.objects.all()
    return render(request, "campus/quizes/results.html", {'marks':marks})

def delete_result(request, myid):
    marks = Marks_Of_User.objects.get(id=myid)
    if request.method == "POST":
        marks.delete()
        return redirect('/results')
    return render(request, "campus/quizes/delete_result.html", {'marks':marks})

# def upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['myfile']
#         print(uploaded_file.name)
#         print(uploaded_file.size)
#         fs = FileSystemStorage()
#         fs.save(uploaded_file.name,uploaded_file)
#         # messages.success(request, 'Your file is uploaded successfully!')
#         return HttpResponse('File uploaded successfully!')
#     return render(request,'campus/upload.html')

# # def pdf_view(request):
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext

# def upload(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile = request.FILES['docfile'])
#             newdoc.save()

#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('list'))
#     else:
#         form = DocumentForm() # A empty, unbound form

#     # Load documents for the list page
#     documents = Document.objects.all()

#     # Render list page with the documents and the form
#     return render( request,
#         'campus/upload.html',
#         {'documents': documents, 'form': form}
#     )

def offerletter(request):
    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']

            Offer_letter(usn=name, my_file=the_files).save()
            
            return HttpResponse("File uploaded!!")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':MyfileUploadForm()
        }      
        
        return render(request, 'campus/OfferLetterUpload.html', context)



def show_file(request):
    all_data = Offer_letter.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/view.html', context)
    

def index(request):
    return render(request,'campus/placementPrepFiles/index.html')

def index1(request):
    return render(request,'campus/placementPrepFiles/index1.html')

    
def index2(request):
    return render(request,'campus/placementPrepFiles/index2.html')

def index3(request):
    return render(request,'campus/placementPrepFiles/index3.html')

def main(request):
    return render(request,'campus/main.html')
def index4(request):
    return render(request,'campus/placementPrepFiles/index4.html')
    
def index5(request):
    return render(request,'campus/placementPrepFiles/index5.html')

def index6(request):
    return render(request,'campus/placementPrepFiles/index6.html')
def index7(request):
    return render(request,'campus/placementPrepFiles/index7.html')



def upload(request):
    if request.method=='POST':
     name=request.POST.get("filename")
     myfile=request.FILES.getlist("uploadfiles")
 

     for f in myfile:
        Java(f_name=name,myfiles=f).save()
     return render(request,'campus/placementPrepFiles/index.html')
        # return redirect('http://127.0.0.1:8000/')


def upload1(request):
    if request.method=='POST':
     name=request.POST.get("filename")
     myfile=request.FILES.getlist("uploadfiles")
  

     for f in myfile:
        C(f_name=name,myfiles=f).save()
        return render(request,'campus/placementPrepFiles/index1.html')
        # return redirect('http://127.0.0.1:8000/')


def upload2(request):
    if request.method=='POST':
     name=request.POST.get("filename")
     myfile=request.FILES.getlist("uploadfiles")
     for f in myfile:
        DBMS(f_name=name,myfiles=f).save()
        # return render(request,'campus/index1.html')
    return render(request,'campus/placementPrepFiles/index2.html')


def upload3(request):
    if request.method=='POST':
     name=request.POST.get("filename")
     myfile=request.FILES.getlist("uploadfiles")
     for f in myfile:
        CN(f_name=name,myfiles=f).save()
    return render(request,'campus/placementPrepFiles/index3.html')


def upload4(request):
    if request.method=='POST':
     name=request.POST.get("filename")
     myfile=request.FILES.getlist("uploadfiles")
     for f in myfile:
        OS(f_name=name,myfiles=f).save()
    return render(request,'campus/placementPrepFiles/index4.html')


def upload5(request):
    if request.method=='POST':
     name=request.POST.get("filename")
     myfile=request.FILES.getlist("uploadfiles")
     for f in myfile:
       ALGO(f_name=name,myfiles=f).save()
    return render(request,'campus/placementPrepFiles/index5.html')


def upload6(request):
    if request.method=='POST':
     name=request.POST.get("filename")
     myfile=request.FILES.getlist("uploadfiles")
     for f in myfile:
         OTHER(f_name=name,myfiles=f).save()
    return render(request,'campus/placementPrepFiles/index6.html')

def upload7(request):
    if request.method=='POST':
     name=request.POST.get("filename")
     myfile=request.FILES.getlist("uploadfiles")
     for f in myfile:
      DS(f_name=name,myfiles=f).save()
    return render(request,'campus/placementPrepFiles/index7.html')



def java(request):
    all_data = Java.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/studentPlacementPrep/java.html', context)

def c(request):
    all_data = C.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/studentPlacementPrep/c.html', context)

def Dbms(request):
    all_data =DBMS.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/studentPlacementPrep/dbms.html', context)

def Algo(request):
    all_data = ALGO.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/studentPlacementPrep/algo.html', context)

def Cn(request):
    all_data =CN.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/studentPlacementPrep/cn.html', context)

def Os(request):
    all_data =OS.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/studentPlacementPrep/os.html', context)

def Other(request):
    all_data = OTHER.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/studentPlacementPrep/others.html', context)

def Ds(request):
    all_data = DS.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'campus/studentPlacementPrep/ds.html', context)

# def send_email(self, request, queryset):
#     form = SendEmailForm(initial={'users': queryset})
#     return render(request, 'users/send_email.html', {'form': form})

def display(request):
    all_data = stu_details.objects.all()

    context = {
        'data':all_data
    }
    return render(request, 'campus/studentDetails.html',context)

def student_companyApplied(request):
    if request.method == 'POST':
        form = studentCompanyApply(request.POST)
        
        if form.is_valid():
            usn = form.cleaned_data['usn']
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']

            studentCompanyApplied(username=usn, name=name, company_name=company).save()
            
            return HttpResponse("Form Submitted")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':studentCompanyApply()
        }      
        
        return render(request, 'campus/studentCompanyApplied/applicationForm.html', context)