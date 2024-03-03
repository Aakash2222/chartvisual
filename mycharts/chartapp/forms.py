from django import forms
from .models import Product
from .models import Signup

class ProductForm(forms.ModelForm):
    class Meta:
        model   = Product
        fields  = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_products': forms.TextInput(attrs={'class': 'form-control'})
        }

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))
    email    = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'}))
    
    class Meta:
        model =  Signup
        fields = ['username','email','password']
