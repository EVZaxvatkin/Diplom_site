from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea
from .models import Promo, Product, Category

CATEGORY = (
    ('вареные колбасы', 'Вареные колбасы'),
    ('варено-копченые колбасы', 'Варено-копченые колбасы'),
    ('полукопченые колбасы', 'Полукопченые колбасы'),
    ('сырокопченые колбасы', 'Сырокопченые колбасы'),
    ('соски и сардельки', 'Сосиски и сардельки'),
    ('колбасы из субпродуктов', 'Колбасы из субпродуктов'),
    ('крупнокусковые полуфабрикаты', 'Крупнокусковые полуфабрикаты'),
    ('мелкокусковые полуфабрикаты', 'Мелкокусковые полуфабрикаты'),
    ('мясные полуфабрикаты', 'Мясные полуфабрикаты'),
    ('пельмени', 'Пельмени'),
    ('фарши', 'Фарши'),
    ('вареники', 'Вареники'),
    ('субпродукты', 'Субпродуты'),
)

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100, widget=forms.PasswordInput)


class PromoForm(forms.ModelForm):
    model = Promo
    fields = ['name', 'product', 'discription', 'start_data', 'end_data']
    widgets = {
        'name': TextInput(attrs={'style': 'width: 100%'}),
        'product': TextInput(attrs={'style': 'width: 100%'}),
        'description': Textarea(attrs={'style': 'width: 100%'})
    }

class ProductForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100, required=False,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите название',
                                      'required': 'True'}))

    category = forms.CharField(label='Категория',
                               required=False,
                               widget=forms.Select(attrs={'required': 'True'}, choices=CATEGORY))

    description = forms.CharField(label='Описание',
                                  max_length=2000,
                                  required=False,
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                      'placeholder': 'Введите описание продукта',
                                      'required': 'True'}))

    image = forms.ImageField(label='Фото продукта', required=False, widget=forms.FileInput(attrs={'required': 'True'}))

