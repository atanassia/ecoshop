from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms

from .models import UsersAdresses, UsersContactPreferences

from django.contrib.auth import views 

non_allowed_username = ['ecoshop', 'djangoeco', 'admineco', 'Лиза дура']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'you@mail.ru'})
        self.fields['email'].required = True
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'user-password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'user-confirm-password', 'placeholder': 'Подтверждение пароля'})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact = email)
        if qs.exists():
            raise forms.ValidationError("Такая почта уже существует")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username in non_allowed_username:
            raise forms.ValidationError("Вы или выбрали зарезервированное имя, или обидели меня. Одно из двух, надеюсь первое.")
        return username


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control'})


class UsersAdressesAddForm(ModelForm):
    class Meta:
        model = UsersAdresses
        fields = ['adress', 'city']

    def __init__(self, *args, **kwargs):
        super(UsersAdressesAddForm, self).__init__(*args, **kwargs)
        self.fields['adress'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['city'].widget = forms.TextInput(attrs={'class': 'form-control'})


class EditUsersAdressesForm(ModelForm):

    # def clean_default_adress(self):
    #     default_adress_value = self.cleaned_data.get("default_adress")
    #     user_id_data = self.cleaned_data.get("user")
    #     data = self.cleaned_data
    #     print(data)
    #     print(user_id_data)
    #     # qs = UsersAdresses.objects.filter(user_id = user_id_data)
    #     # if default_adress_value==True and default_adress_value in qs:
    #     #     raise forms.ValidationError('Вы не можете сделать этот адрес дефолтным')
    #     # return default_adress_value

    class Meta:
        model = UsersAdresses
        fields = ['adress', 'city', 'default_adress']
    
    def __init__(self, *args, **kwargs):
        super(EditUsersAdressesForm, self).__init__(*args, **kwargs)
        self.fields['adress'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['city'].widget = forms.TextInput(attrs={'class': 'form-control'})



class UsersContactPreferencesForm(ModelForm):
    class Meta:
        model = UsersContactPreferences
        fields = ['phone', 'phone_send','whatsapp', 'email_send', 'instagram', 'instagramm_send']

    def __init__(self, *args, **kwargs):
        super(UsersContactPreferencesForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['instagram'].widget = forms.TextInput(attrs={'class': 'form-control'})