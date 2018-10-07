# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import m_inventory,m_pengajuan,m_user
from django.db.models import Q
import datetime

# Create your views here.
def save(request):
    if request.method == "POST":
        nis = request.POST.get('nis', False)
        nama = request.POST.get('nama', False)
        nohp = request.POST.get('nohp', False)
        item = request.POST.get('item', False)
        jabatan = request.POST.get('jabatan', False)
        tanggal = request.POST.get('tanggal', False)
        waktu = request.POST.get('waktu', False)
        kegunaan = request.POST.get('kegunaan', False)
        flag = '1'
        if jabatan == "DLL":
            flag = '2'
        object = m_pengajuan(nis=nis, nama=nama, nohp=nohp, item=item, jabatan=jabatan, kegunaan=kegunaan, flag=flag, tanggal=tanggal, waktu=waktu)
        object.save()
        return redirect('/done')
    else:
        return redirect('/peminjaman')

def index(request):
    now = datetime.date.today()
    print (now)
    query = m_pengajuan.objects.filter(tanggal=now)

    for items in query:
        ids = items.item
        ruangan = m_inventory.objects.get(id=ids)
        items.item = ruangan.nama
        if items.flag == 1:
            items.flag = "Proses Persetujuan DPO"
        if items.flag == 2:
            items.flag = "Proses Persetujuan Wakasek bid. Sarpas"
        if items.flag == 3:
            items.flag = "Disetujui"
        if items.flag == 4:
            items.flag = "Ditolak"

    response = {
        "objects":query
    }
    return render(request, "index.html", response)

def items(request):
    return render(request,"items.html")    

def peminjaman(request):
    query = m_inventory.objects.all()
    
    response = {
        "objects" : query
    }
    return render(request,"peminjaman.html", response)

def login(request):
    return render(request, "login.html")

def login_check(request):
    username = request.POST["username"]
    password = request.POST["pass"]

    try:
        query = m_user.objects.get(nama=username,password=password)
        request.session['username'] = query.nama
        request.session['jabatan'] = query.jabatan
        return redirect ('/admin_peminjaman')
   
    except m_user.DoesNotExist:
        return redirect ('/login')
        

def admin_peminjaman(request):

    if request.session.has_key('username'):

        jabatan = request.session['jabatan']
        print (jabatan)

        if jabatan != "SARPRAS" and jabatan != "DPO":
            query = m_pengajuan.objects.filter(jabatan=jabatan)
        elif jabatan == "DPO":
            query1 = m_pengajuan.objects.filter(jabatan="PO")
            query2 = m_pengajuan.objects.filter(jabatan="PK")
            query = query1 | query2
        elif jabatan == "SARPRAS":
            query1 = m_pengajuan.objects.filter(jabatan="DLL")
            query2 = m_pengajuan.objects.filter(flag__gt =  "1")
            query = query1 | query2
            inventory = True


        if query.exists():
            for items in query:
                ids = items.item
                status = items.flag
                ruangan = m_inventory.objects.get(id=ids)
                items.item = ruangan.nama
                if items.flag == 1:
                    items.flag = "Proses Persetujuan DPO"
                if items.flag == 2:
                    items.flag = "Proses Persetujuan Wakasek bid. Sarpas"
                if items.flag == 3:
                    items.flag = "Disetujui"
                if items.flag == 4:
                    items.flag = "Ditolak"

            response = { 
                "objects":query 
            }

        else:
            response = {}
        return render(request, "admin_peminjaman.html", response)
    
    else:
        return redirect('/login')
   

def logout(request):
    del request.session['username']
    del request.session['jabatan']
    return redirect('/login')

def admin_details(request, id):
    button = []
    if request.session.has_key('username'):
        jabatan = request.session['jabatan']
        query = m_pengajuan.objects.get(id=id)
        ids = query.item
        ruangan = m_inventory.objects.get(id=ids)
        query.item = ruangan.nama
        if jabatan != "SARPRAS" and query.flag > 1:
            button = False
        elif query.flag == 3 or query.flag == 4 :
            button = False
        elif jabatan == "SARPRAS" and query.flag > 1:
            inventory = True
            button = True
        else :
            button = True
        if query.flag == 1:
            query.flag = "Proses Persetujuan DPO"
        if query.flag == 2:
            query.flag = "Proses Persetujuan Wakasek bid. Sarpas"
        if query.flag == 3:
            query.flag = "Disetujui"
        if query.flag == 4:
            query.flag = "Ditolak"



    response = {
        "objects":query,
        "button":button
    }
    return render(request, 'admin_details.html', response)

def admin_verify(request):
    id = request.POST.get('id', False)
    setuju = request.POST.get('button', False)
    print (id)
    print (setuju)
    query = m_pengajuan.objects.get(id=id)
    search = m_pengajuan.objects.filter(id=id)
    status = query.flag
    print (status)

    if setuju == "Setuju":
        stat_baru =  status + 1

    elif setuju == "Tolak":
        stat_baru = 4

    print (stat_baru)
    
    search.update(flag=stat_baru)

    return redirect('/admin_peminjaman')

def done(request):
    return render(request, 'done.html')

def cari(request):
    query = m_pengajuan.objects.order_by('-timestamp')

    for items in query:
        ids = items.item
        ruangan = m_inventory.objects.get(id=ids)
        items.item = ruangan.nama
        if items.flag == 1:
            items.flag = "Proses Persetujuan DPO"
        if items.flag == 2:
            items.flag = "Proses Persetujuan Wakasek bid. Sarpas"
        if items.flag == 3:
            items.flag = "Disetujui"
        if items.flag == 4:
            items.flag = "Ditolak"

    response = {
        "objects":query
    }
    return render(request, "cari.html", response)

def admin_inventory(request):
    
    if request.session.has_key('username'):
        jabatan = request.session['jabatan']
        if jabatan == "SARPRAS":
            inventory = True

        query = m_inventory.objects.all()
        response = {
            "objects":query
        }
        return render (request, 'admin_inventory.html',response)
    
    else:
        return redirect ('/login')

def admin_inventory_add(request):
 
    if request.session.has_key('username'):
        jabatan = request.session['jabatan']
        if jabatan == "SARPRAS":
            inventory = True

        return render (request, 'admin_inventory_add.html')

def admin_inventory_save(request):
    if request.method == "POST":
        kategori = request.POST.get('kategori', False)
        lokasi = request.POST.get('lokasi', False)
        nama = request.POST.get('nama', False)
        object = m_inventory(kategori=kategori, lokasi=lokasi, nama=nama)
        object.save()
        return redirect('/admin_inventory')
    else:
        return redirect('/admin_inventory_add')