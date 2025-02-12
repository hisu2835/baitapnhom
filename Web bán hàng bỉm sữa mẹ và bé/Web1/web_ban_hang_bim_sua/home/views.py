from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from webbs.models import DanhMuc,SanPham,KhachHang,DonHang,ChiTietDonHang,GioHang,ChiTietGioHang
from .forms import DanhMucForm,KhachHangForm
from django.core.cache import cache
from elasticsearch_dsl import Q
from webbs.document import DanhMucDocument
from django.views.decorators.cache import cache_page
# Create your views here.

# Cache trang danh mục trong 15 phút
# @cache_page(60 * 15)
def danhmuc(request):
    danhmucs = cache.get('danhmucs')
    if not danhmucs:
        danhmucs = DanhMuc.objects.all()
        cache.set('danhmucs', danhmucs, timeout=60 * 3)
    
    template = loader.get_template('home/danhmuc/danhmucs.html')
    context = {'danhmucs': danhmucs}
    return HttpResponse(template.render(context, request))

def danhmuc_edit(request, id):
    danhmuc = get_object_or_404(DanhMuc, id=id)
    template = loader.get_template('home/danhmuc/danhmuc-edit.html')
    context = {'danhmuc': danhmuc}
    return HttpResponse(template.render(context, request))

def danhmuc_delete(request, id):
    if request.method == "POST":
        danhmuc = get_object_or_404(DanhMuc, id=id)
        danhmuc.delete()
        return redirect("/danhmucs")
    template = loader.get_template('home/danhmuc/danhmuc-delete.html')
    context = {'danhmuc': get_object_or_404(DanhMuc, id=id)}
    return HttpResponse(template.render(context, request))

def danhmuc_new(request):
    if request.method == "POST":
        form = DanhMucForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/danhmucs")
    template = loader.get_template('home/danhmuc/danhmuc-new.html')
    return HttpResponse(template.render({}, request))

# Quản lý khách hàng
def khachhang(request):
    khachhangs = KhachHang.objects.all()
    template = loader.get_template('home/khachhang/khachhangs.html')
    context = {'khachhangs': khachhangs}
    return HttpResponse(template.render(context, request))

def khachhang_edit(request, id):
    khachhang = get_object_or_404(KhachHang, id=id)
    template = loader.get_template('home/khachhang/khachhang-edit.html')
    context = {'khachhang': khachhang}
    return HttpResponse(template.render(context, request))

def khachhang_delete(request, id):
    if request.method == "POST":
        khachhang = get_object_or_404(KhachHang, id=id)
        khachhang.active = False
        khachhang.save()
        return redirect("/khachhangs")
    template = loader.get_template('home/khachhang/khachhang-delete.html')
    context = {'khachhang': get_object_or_404(KhachHang, id=id)}
    return HttpResponse(template.render(context, request))

def khachhang_new(request):
    if request.method == "POST":
        form = KhachHangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/khachhangs")
    template = loader.get_template('home/khachhang/khachhang-new.html')
    return HttpResponse(template.render({}, request))
