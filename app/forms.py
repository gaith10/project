from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

attrs = {'class': 'forms-control'}
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='إسم المستخدم',
        widget=forms.TextInput(attrs=attrs)

    )
    password = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs=attrs)

    )


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label='الإسم الأول',
        widget=forms.TextInput(attrs=attrs)

    )

    last_name = forms.CharField(
        label='لقب العائلة',
        widget=forms.TextInput(attrs=attrs)

    )

    
    username = forms.CharField(
        label='إسم المستخدم',
        widget=forms.TextInput(attrs=attrs)

    )
 
    email = forms.EmailField(
        label='البريد الإلكتروني',
        widget=forms.TextInput(attrs=attrs)

    )  

    password1 = forms.CharField(
        label='كلمة المرور',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)

    )

    password2 = forms.CharField(
        label='تأكيد كلمة المرور',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)

    )

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name','username', 'email')
class ProfileForm(UserChangeForm):
    password = None

    class Meta : 
        model = User
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),


        }