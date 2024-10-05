from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, 'index.html')
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to registration success page
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def user_login(request):
    # Your login logic goes here
    return render(request, 'user_login.html')  # Replace 'user_login.html' with the actual template name
def company_login(request):
    # Your login logic goes here
    return render(request, 'company_login.html')  # Replace 'company_login.html' with the actual template name

def choose(request):
    # Your view logic here
    return render(request, 'choose.html')
def admin(request):
    return render(request,'admin.html')



def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')