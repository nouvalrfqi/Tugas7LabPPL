from django.shortcuts import render

# Daftar produk ban mobil
PRODUK_LIST = [
    {"id": 1, "nama": "Ban Mobil All-Terrain", "deskripsi": "Ban tangguh untuk segala medan, cocok untuk SUV dan off-road.", "harga": 1200000, "gambar": "ban_all_terrain.jpg"},
    {"id": 2, "nama": "Ban Mobil Performance", "deskripsi": "Ban performa tinggi untuk kecepatan dan stabilitas maksimal di jalan raya.", "harga": 1500000, "gambar": "ban_performance.jpg"},
    {"id": 3, "nama": "Ban Mobil Hemat Bahan Bakar", "deskripsi": "Dirancang untuk efisiensi bahan bakar dan kenyamanan berkendara.", "harga": 950000, "gambar": "ban_eco.jpg"},
]

def home(request):
    return render(request, 'katalog/home.html')

def produk_list(request):
    return render(request, 'katalog/produk_list.html', {"produk_list": PRODUK_LIST})

def produk_detail(request, id):
    produk = next((p for p in PRODUK_LIST if p["id"] == id), None)
    if not produk:
        return render(request, 'katalog/produk_detail.html', {
            "produk": {
                "nama": "Produk tidak ditemukan", 
                "deskripsi": "Produk dengan ID ini tidak tersedia.", 
                "harga": 0
            }
        })
    return render(request, 'katalog/produk_detail.html', {"produk": produk})

def kontak(request):
    return render(request, 'katalog/kontak.html')

def tentang(request):
    return render(request, 'katalog/tentang.html')

def keranjang(request):
    return render(request, 'katalog/keranjang.html')
