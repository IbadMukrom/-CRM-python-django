from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('produk/', views.produk, name="produk"),
    path('pelanggan/<int:id>/', views.pelanggan, name='pelanggan'),

    path('tambah_pelanggan/', views.tambah_pelanggan, name='tambah_pelanggan'),

    path('tambah_produk/', views.tambah_produk, name='tambah_produk'),
    path('update_produk/<int:id>/', views.update_produk, name='update_produk'),
    path('hapus_produk/<int:id>/', views.hapus_produk, name='hapus_produk'),


    path('buatpesanan/', views.buat_pesanan, name='buatpesanan'),
    path('update_pesanan/<int:id>/', views.update_pesanan, name='update_pesanan'),
    path('delete_pesanan/<int:id>/', views.delete_pesanan, name='delete_pesanan'),
    path('signup/', views.signup, name='signup'),


]