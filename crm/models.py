from django.db import models


# Create your models here.

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100, null=True )
    no_hp = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    KATEGORI = (
        ('Olahraga', 'Olahraga'),
        ('Edukasi', 'Edukasi'),
        ('Hiburan','Hiburan'),
    )
    nama = models.CharField(max_length=50, null=True)
    harga = models.FloatField(null=True)
    kategori = models.CharField(max_length=20, null=True, choices=KATEGORI)
    deskripsi = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.nama

class Pesanan(models.Model):
    STATUS = (
        ('Tertunda', 'Tertunda'),
        ('Terkirim', 'Terkirim'),
        ('Dalam Perjalan', 'Dalam Perjalan'),
        
    )
    pelanggan = models.ForeignKey (Pelanggan, null=True, on_delete=models.SET_NULL)
    produk = models.ForeignKey (Produk, null= True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField (auto_now_add=True, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    def __str__(self):
        return self.produk.nama




