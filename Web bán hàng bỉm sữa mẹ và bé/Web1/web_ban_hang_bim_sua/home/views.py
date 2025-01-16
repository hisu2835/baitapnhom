from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from webbs.models import DanhMuc

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def danh_muc(request):
    danh_muc = danh_muc.objects.all()
    template = loader.get_template('home/webbimsua.html')
    context = {
        'danh_muc': danh_muc,
    }
    return HttpResponse(template.render(context, request))

def edit_danh_muc(request):
    danh_muc = danh_muc.objects.get(id = 1)
    template = loader.get_template('home/webbs_edit.html')
    context = {
        'danh_muc': danh_muc,
    }
    return HttpResponse(template.render(context, request))