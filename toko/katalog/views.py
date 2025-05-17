from django.shortcuts import render

# Daftar produk sederhana
PRODUK_LIST = [
    {"id": 1, "nama": "Kopi Gayo", "deskripsi": "Kopi arabika premium dari dataran tinggi Gayo.", "harga": 50000, "gambar": "kopi_gayo.jpg"},
    {"id": 2, "nama": "Teh Hijau", "deskripsi": "Teh hijau organik kaya antioksidan.", "harga": 30000, "gambar": "teh_hijau.jpg"},
    {"id": 3, "nama": "Madu Hutan", "deskripsi": "Madu asli dari lebah hutan liar.", "harga": 75000, "gambar": "madu_hutan.jpg"},
]

def home(request):
    return render(request, 'katalog/home.html')

def produk_list(request):
    return render(request, 'katalog/produk_list.html', {"produk_list": PRODUK_LIST})

def produk_detail(request, id):
    produk = next((p for p in PRODUK_LIST if p["id"] == id), None)
    if not produk:
        return render(request, 'katalog/produk_detail.html', {"produk": {"nama": "Produk tidak ditemukan", "deskripsi": "Produk dengan ID ini tidak tersedia.", "harga": 0}})
    return render(request, 'katalog/produk_detail.html', {"produk": produk})

def kontak(request):
    return render(request, 'katalog/kontak.html')

def tentang(request):
    return render(request, 'katalog/tentang.html')

def keranjang(request):
    return render(request, 'katalog/keranjang.html')
