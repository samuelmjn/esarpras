"""sarpras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from peminjam.views import index,save,items,peminjaman,login,login_check,admin_peminjaman,logout,admin_details,admin_verify,done,cari,admin_inventory,admin_inventory_add,admin_inventory_save
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^save/', save),
    url(r'^$', index),
    url(r'^items/', items),
    url(r'^peminjaman/', peminjaman),
    url(r'^login/', login),
    url(r'^login_check/', login_check),
    url(r'^admin_peminjaman/', admin_peminjaman),
    url(r'^logout/', logout),
    url(r'^admin_details/(?P<id>\d+)', admin_details),
    url(r'^admin_verify/', admin_verify),
    url(r'^done/', done),
    url(r'^cari/', cari),
    url(r'^admin_inventory/', admin_inventory),
    url(r'^admin_inventory_add/', admin_inventory_add),
    url(r'^admin_inventory_save/', admin_inventory_save),
]
