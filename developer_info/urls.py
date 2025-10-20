"""
开发者信息应用路由配置
"""

from django.urls import path
from . import views

app_name = 'developer_info'

urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section")
]