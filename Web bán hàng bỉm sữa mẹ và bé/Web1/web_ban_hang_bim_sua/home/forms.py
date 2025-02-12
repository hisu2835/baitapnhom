from django import forms
from .models import SanPham, DonHang, ChiTietDonHang, GioHang, ChiTietGioHang

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = '__all__'

class DonHangForm(forms.ModelForm):
    class Meta:
        model = DonHang
        fields = '__all__'