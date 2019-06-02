from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from app.models import User
from django import forms
from django.forms import ModelForm
from app.models import Contact
from app.models import Request

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'name',)
        labels = {'email': 'メールアドレス','name': '名前',}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '例) 代行　エンジン'}),
            'email': forms.TextInput(attrs={'placeholder': '例) daico-engine@gmail.com'}),
        }

class UserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('email', 'name', 'sex', 'birth_year', 'birth_month','birth_day', 'address', 'phone')
        labels = {'email': 'メールアドレス','name': '名前','sex': '性別','birth_year': '西暦','birth_month': '生誕月','birth_day': '生誕日','address': '住所','phone': '電話番号',}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '例) 代行　エンジン'}),
            'birth_year': forms.TextInput(attrs={'placeholder': '例) 1996'}),
            'birth_month': forms.TextInput(attrs={'placeholder': '例) 4'}),
            'birth_day': forms.TextInput(attrs={'placeholder': '例) 29'}),
            'phone': forms.TextInput(attrs={'placeholder': '例) 09065668268'}),
            'address': forms.TextInput(attrs={'placeholder': '例) 東京都中野区'}),
        }

# class MyPasswordChangeForm(PasswordChangeForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'name', 'foo', 'message', 'phone')
        labels = {'email': 'メールアドレス','name': '名前','foo': 'お問い合わせ種類','message': 'お問い合わせ内容','phone': '電話番号',}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '例) 代行　エンジン'}),
            'email': forms.TextInput(attrs={'placeholder': '例) neekey@gmail.com'}),
            'message': forms.TextInput(attrs={'placeholder': '例) パスワードを忘れてしまいました'}),
            'phone': forms.TextInput(attrs={'placeholder': '例) 09065668268'}),
        }

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'kind', 'email', 'phone', 'address', 'message')
        labels = {'email': 'メールアドレス','name': '名前','kind': '貴店の業種','message': '要望','phone': '電話番号', 'address': '住所',}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '担当者名'}),
            'email': forms.TextInput(attrs={'placeholder': '例) neekey@gmail.com'}),
            'message': forms.TextInput(attrs={'placeholder': '例) 掲載したいです'}),
            'phone': forms.TextInput(attrs={'placeholder': '例) 09065668268'}),
            'address': forms.TextInput(attrs={'placeholder': '例) 東京都港区浜松町'}),
            'kind': forms.TextInput(attrs={'placeholder': '例) 家事代行、育児代行'}),
        }