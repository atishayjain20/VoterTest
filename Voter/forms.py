from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#hello
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    aadhar = forms.CharField(max_length=12)
    contactno = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username',  'password1',
                  'password2', 'aadhar', 'email', 'contactno']
        exclude = ['contactno']


# class registrationTest(UserRegisterForm):
#     class Meta:
#         model = User
#         exclude = ['contactno']
