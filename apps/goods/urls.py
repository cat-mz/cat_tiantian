# from django.conf.urls import url
from django.urls import path,re_path
from apps.goods.views import IndexView, DetailView, ListView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    re_path(r'^goods/(?P<goods_id>\d+)$',DetailView.as_view(),name='detail'),# 详情页
    re_path(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 列表页
    #nginx 版
    # url(r'^index$', IndexView.as_view(), name='index'), # 首页
]
