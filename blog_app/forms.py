from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Article


class PostArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'image', 'tags')

        widgets = {
            'title': forms.Textarea(attrs=
                                    {'rows': 1, 'cols': 90}),
            'text': forms.Textarea(attrs=
                                   {'rows': 20, 'cols': 90}),
            'tags': forms.SelectMultiple(attrs=
                                    {'size': 9}),
        }


class ContactForm(forms.Form):

    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='Eメール', max_length=30)
    text = forms.CharField(label='お問い合わせ内容', min_length=20, max_length=200, widget=forms.Textarea)


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    # username = forms.CharField(label="ユーザー名", max_length=50)
    # password = forms.CharField(label="パスワード", widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': "ユーザー名とパスワードに誤りがあります。",
    }
