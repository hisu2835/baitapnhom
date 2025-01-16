from django.db import models

# Mô hình danh mục
class DanhMuc(models.Model):
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)
    hinh_anh = models.ImageField(upload_to='danh_muc/', null=True, blank=True)

    def __str__(self):
        return self.ten

    class Meta:
        verbose_name_plural = 'Danh mục'

# Mô hình sản phẩm
class SanPham(models.Model):
    ten = models.CharField(max_length=100)
    danh_muc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    mo_ta = models.TextField(blank=True)
    hinh_anh = models.ImageField(upload_to='san_pham/', null=True, blank=True)
    so_luong_ton = models.IntegerField(default=0)
    thuong_hieu = models.CharField(max_length=100)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_cap_nhat = models.DateTimeField(auto_now=True)
    hoat_dong = models.BooleanField(default=True)

    def __str__(self):
        return self.ten

# Mô hình khách hàng
class KhachHang(models.Model):
    ten = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    so_dien_thoai = models.CharField(max_length=15)
    dia_chi = models.TextField()
    ngay_tao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ten

# Mô hình đơn hàng
class DonHang(models.Model):
    TRANG_THAI_CHOICES = [
        ('cho_xac_nhan', 'Chờ xác nhận'),
        ('da_xac_nhan', 'Đã xác nhận'),
        ('dang_giao', 'Đang giao'),
        ('da_giao', 'Đã giao'),
        ('da_huy', 'Đã hủy'),
    ]

    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    tong_gia = models.DecimalField(max_digits=10, decimal_places=2)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI_CHOICES, default='cho_xac_nhan')
    dia_chi_giao_hang = models.TextField()
    trang_thai_thanh_toan = models.BooleanField(default=False)

    def __str__(self):
        return f"Đơn hàng {self.id} của {self.khach_hang}"

# Mô hình chi tiết đơn hàng
class ChiTietDonHang(models.Model):
    don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong = models.IntegerField()
    gia_tien = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.so_luong} của {self.san_pham.ten} trong đơn hàng {self.don_hang.id}"

# Mô hình giỏ hàng
class GioHang(models.Model):
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Giỏ hàng {self.id} của {self.khach_hang}"

# Mô hình chi tiết giỏ hàng
class ChiTietGioHang(models.Model):
    gio_hang = models.ForeignKey(GioHang, on_delete=models.CASCADE)
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.so_luong} của {self.san_pham.ten} trong giỏ hàng {self.gio_hang.id}"