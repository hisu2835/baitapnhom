from django.shortcuts import render
from .models import DanhMuc, SanPham

def home(request):
    san_pham = SanPham.objects.all()
    danh_muc = DanhMuc.objects.all()
    context = {
        'san_pham': san_pham,
        'danh_muc': danh_muc,
    }
    return render(request, 'home/home.html', context)