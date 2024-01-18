from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'placeholder':'please user name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'please enter email'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'please enter first name name'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'please enter last name'}))
    password_1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'please enter a password'}))
    password_2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'enter your password again'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exist')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل تکراری است')
        else:
            return email


    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('password not match')
        elif len(password2)<8:
            raise forms.ValidationError('پسوورد باید حداقل 8 کاراکتر باشد')
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('باید پسوورد دارای حداقل یک حرف بزرگ باشد')
        else:
            return password1

#---------------------

class UserLoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()


#------------------------------change pass

class ChangePasswordForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput())
    new_password1=forms.CharField(widget=forms.PasswordInput())
    new_password2=forms.CharField(widget=forms.PasswordInput())





