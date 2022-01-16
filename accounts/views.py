from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm

from .forms import StudentSignUpForm, TeacherSignUpForm, AdminSignUpForm
from .models import User


def accounts_home(request):
    return render(request, '../templates/index.html')


def register(request):
    return render(request, '../templates/register.html')

class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = '../templates/student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class teacher_register(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = '../templates/teacher_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class admin_register(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = '../templates/admin_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                if user.is_teacher:
                    return HttpResponseRedirect('https://www.theguardian.com/teacher-network/2017/aug/15/ten-books-every-teacher-should-read')
                    # return redirect('teacher_dashboard')
                elif user.is_student:
                    return HttpResponseRedirect('https://rau.am/')
                    # return redirect('student_dashboard')
                else:
                    return redirect('../../admin')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html', context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('home')
