from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm,ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def contactus(request):
    return render(request,'contactus/contactus_page.html')

def user_register(request):
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        if form_register.is_valid():
            data = form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password_1'],)
            return redirect('home:home-func')

    else:
        form_register = UserRegisterForm()
    contex = {'form_register': form_register}
    return render(request,'contactus/user_register.html',contex)

    # return render(request,'contactus/user_register.html')

#-----------------------log in
def user_login(request):
    if request.method == 'POST':
        form_login = UserLoginForm(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(request,username=data['user'],
                                password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('home:home-func')

    else:
        form_login = UserLoginForm()
    return render(request,'contactus/login.html',{'form_login':form_login})
#-----------------log out
def user_logout(request):
    logout(request)
    return redirect('home:home-func')
#----------------------change pass




@login_required()
def change_password(request):
    if request.method=='POST':
        user=request.user
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            old_password=data['old_password']
            new_password1=data['new_password1']
            new_password2=data['new_password2']
            # if old_password!=user.password:
            if not user.check_password(old_password):
                return HttpResponse('پسوورد درست نیست')
            elif new_password1!=new_password2:
                return HttpResponse('پسوورد شما با هم مطابقت ندارد')
            else:
                user.set_password(new_password1)
                login(request,user)
                user.save()
                return HttpResponse('پسوورد تغییر یافت')

    else:
        form=ChangePasswordForm()
    return render(request,'contactus/changepassword.html',{'form':form})












