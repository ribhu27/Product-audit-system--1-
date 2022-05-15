from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, Student
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from .models import Student


# Create your views here.

# Calculation of Test Scores
class Sum:
    def __init__(self,SITW,SIOT,SS,SClang):
        self.SITW=SITW
        self.SIOT=SIOT
        self.SS=SS
        self.SClang=SClang
        self.Perc=(SClang+SIOT+SS+SITW)/400*100
        self.GPA=self.Perc/9.5*100

# Homepage
def home(request):
    return render(request,'home.html')

# Result Page
def result(request):
    global stud
    x=int(request.POST['username'])
    stud=Student.objects.get(roll_number=x)
    return render(request,'result.html',{'stu':stud})

# Login Page
def login(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                stud=Student.objects.filter(roll_number=request.username)
                return redirect('result')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')
        else: 
            return render(request,'login.html')

# Contact us
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        prob = request.POST.get('prob')
        contact = Contact(name=name, email=email, prob=prob, date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been sent!!!")
    return render(request,'contact.html')

# For logging out
def logout(request):
    messages.info(request,"Session Logged Out")
    return redirect('home')

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'
    error_message = ''
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                error_message = 'Roll number already exists.'
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                error_message = 'Email already exists.'
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                error_message = 'Passwords do not match.'

            else:
                try:
                    # Create the user:
                    user = Student.objects.create(
                        
                        name = request.POST['name'],
                        roll_number = request.POST['username'],
                        email= request.POST['email'],
                        password = request.POST['password'],
                        branch= request.POST['branch']
                    )
                    user.name = form.cleaned_data['name']
                    #user.last_name = form.cleaned_data['last_name']
                    # user.phone_number = form.cleaned_data['phone_number']
                    user.save()
                
                    # Login the user
                    login(request)
                
                    # redirect to accounts page:
                    return redirect('home')
                except Exception as e:
                    form = RegisterForm()
                    error_message='An error occured'
                    return render(request, template, {'form': form, 'error_message' : error_message})                   


   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form, 'error_message' : error_message})
# The end