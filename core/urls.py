from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home_view, name="homepage"),
    path('bangtuongtac/', bangtuongtac_view, name="bangtuongtac-view"),
    path('dichvu/', dichvu_view, name="dichvu-view"),
    path('dichvubaotribaohanhmay/', dichvubaotribaohanhmay_view, name="dichvubaotribaohanhmay-view"),
    path('dichvuthuemayphotocopy/', dichvuthuemayphotocopy_view, name="dichvuthuemayphotocopy-view"),
    path('giohang/', giohang_view, name="giohang-view"),
    path('manhinhghep/', manhinhghep_view, name="manhinhghep-view"),
    path('maychieu/', maychieu_view, name="maychieu-view"),
    path('mayphoto/', mayphoto_view, name="mayphoto-view"),
    path('printscan/', printscan_view, name="printscan-view"),
    path('thongbaobaotrimay/', thongbaobaotrimay_view, name="thongbaobaotrimay-view"),
    path('tintuc/', tintuc_view, name="tintuc-view"),
    path('vechungtoi/', vechungtoi_view, name="vechungtoi-view"),
    path('updateItem/', updateItem_view, name="update-item"),
    path('checkout/', checkout_view, name="checkout-view"),
]