from crm.models import Pesanan, Pelanggan,Produk
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class PesananForm(ModelForm):
    class Meta:
        model = Pesanan
        fields = '__all__'

class PelangganForm(ModelForm):
    class Meta:
        model = Pelanggan
        fields = '__all__'

class ProdukForm(ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

class Signupform(UserCreationForm):
    nama_depan = forms.CharField(max_length=50)
    nama_belakang = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    
    class Meta:
        model = User
        fields = ('username', 'nama_depan', 'nama_belakang', 'email', 'password1', 'password2')