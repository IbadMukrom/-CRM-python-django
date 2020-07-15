from django.shortcuts import render, redirect
from .models import *
from .forms import PesananForm, PelangganForm, ProdukForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

@login_required
def home (request):
    pesanan = Pesanan.objects.all()
    pelanggans = Pelanggan.objects.all()
    total_pelanggans = pelanggans.count()
    total_pesanan = pesanan.count()
    terkirim = pesanan.filter(status='Terkirim').count()
    tertunda = pesanan.filter(status='Tertunda').count()

    context = {'pesanan': pesanan, 'pelanggans':pelanggans,
    'total_pesanan': total_pesanan, 'terkirim': terkirim,
    'tertunda': tertunda, 'total_pelanggans':total_pelanggans}

    return render (request,'crm/dashboard.html',context)

@login_required
def produk (request):
    produk = Produk.objects.all()
    return render (request, 'crm/produk.html', {'produk':produk})

@login_required
def tambah_produk(request):
    form = ProdukForm()
    if request.method=='POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produk/')
    context = {'form': form}
    return render(request, 'crm/produk_form.html', context)

@login_required
def update_produk(request, id):
    produk = Produk.objects.get(id = id)
    form = ProdukForm(instance=produk)
    
    if request.method=='POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect ('/produk/')
    context = {'form': form}
    return render (request,'crm/produk_form.html', context)


@login_required
def hapus_produk(request, id):
    produk=Produk.objects.get(id=id)
    produk.delete()
    return redirect('/produk/')

@login_required
def pelanggan(request, id):
    pelanggan = Pelanggan.objects.get(id=id)
    
    pesanan = pelanggan.pesanan_set.all()
    pesanan_count = pesanan.count()
    context = {'pelanggan':pelanggan, 'pesanan': pesanan,'pesanan_count': pesanan_count}
    return render (request, 'crm/pelanggan.html', context)

@login_required
def tambah_pelanggan(request):
    form = PelangganForm()
    if request.method=='POST':
        form =PelangganForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'crm/pelanggan_form.html', context)

@login_required
def buat_pesanan(request):
    form = PesananForm()
    if request.method == 'POST':
        form = PesananForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    
    context = {'form': form}
    return render (request, 'crm/pesanan_form.html', context)

@login_required
def update_pesanan (request, id):
    pesanan = Pesanan.objects.get(id=id)
    form = PesananForm(instance=pesanan)
    
    if request.method=='POST':
        form = PesananForm(request.POST, instance=pesanan)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render (request,'crm/pesanan_form.html', context)

@login_required
def delete_pesanan (request, id):
    pesanan = Pesanan.objects.get(id=id)
    pesanan.delete()
    return redirect ('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login = (request, user)
            messages.success(request, 'akun berhasil di buat')
            return redirect('/accounts/login/?next=/')
        else:
            form = UserCreationForm()
            messages.warning(request,'pastikan username dan password anda benar !!')
            return render (request, 'registration/signup.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form':form})