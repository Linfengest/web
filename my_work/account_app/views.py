from django.shortcuts import render
from . import forms as myforms
from django.contrib.auth import authenticate,login
from django.shortcuts import reverse,redirect
from django.contrib.auth.models import User

# Create your views here.
def login_my(request):
    if request.method == 'GET':
        login_form = myforms.login_form()
        return render(request,'account/login.html',{'form':login_form})

    if request.method == 'POST':
        login_form = myforms.login_form(request.POST)
        if login_form.is_valid() :
            data = login_form.cleaned_data
            user = authenticate(username=data['name'],password=data['password'])
            if user :
                login(request,user)
                return redirect(reverse('blog:index'))
            else :
                return render(request,'account/login_error.html')
        else :
            return render(request, 'account/login_error.html')

    pass


def register_my(request):
    if request.method == 'GET' :
        form = myforms.register_form()
        return render(request,'account/register.html',{'form':form})

    if request.method == 'POST' :
        form = myforms.register_form(request.POST)
        if form.is_valid() :
            # data = form.cleaned_data
            # user_list = User.objects.all()
            # print(data['username'])
            # print(user_list)
            # if data['username'] in user_list :
            #     return render(request,'account/register3.html')
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request,'account/register1.html')
        else:
            return render(request,'account/register2.html')
