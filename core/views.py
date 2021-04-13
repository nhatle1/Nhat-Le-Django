from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html', {})

def dichvu_view(request):
    return render(request, 'dichvu.html', {})

def bangtuongtac_view(request):
    return render(request, 'bangtuongtac.html', {})

def dichvubaotribaohanhmay_view(request):
    return render(request, 'dichvubaotribaohanhmay.html', {})

def dichvuthuemayphotocopy_view(request):
    return render(request, 'dichvuthuemayphotocopy.html', {})

def giohang_view(request):
    return render(request, 'giohang.html', {})

def manhinhghep_view(request):
    return render(request, 'manhinhghep.html', {})

def maychieu_view(request):
    return render(request, 'maychieu.html', {})

def mayphoto_view(request):
    return render(request, 'mayphoto.html', {})

def tintuc_view(request):
    return render(request, 'tintuc.html', {})

def vechungtoi_view(request):
    return render(request, 'vechungtoi.html', {})

def printscan_view(request):
    return render(request, 'printScan.html', {})

def thongbaobaotrimay_view(request):
    return render(request, 'thongbaobaotrimay.html', {})