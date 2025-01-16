from django.contrib import admin
from .models import DanhMuc, SanPham, KhachHang, DonHang, ChiTietDonHang, GioHang, ChiTietGioHang

admin.site.register(DanhMuc)
admin.site.register(SanPham)
admin.site.register(KhachHang)
admin.site.register(DonHang)
admin.site.register(ChiTietDonHang)
admin.site.register(GioHang)
admin.site.register(ChiTietGioHang)