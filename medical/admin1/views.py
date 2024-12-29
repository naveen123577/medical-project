from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from main.models import rent_tbl
from vendor.models import venderreg_tbl
# Create your views here.
from django.shortcuts import render,redirect
from main.models import product_tbl,reg_tbl,adminreg_tbl,order_tbl,order_payment
# Create your views here.

def adminindex(request):
    obj=product_tbl.objects.all()
    return render(request,'admindash.html',{'data':obj})

def userview(request):
    obj=reg_tbl.objects.all()
    return render(request,'userview.html',{'data':obj})

def sellerview(request):
    obj=venderreg_tbl.objects.all()
    return render(request,'sellerview.html',{'data':obj})


def deleteuser(request):
    idno=request.GET.get("idn")
    obj=reg_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect('/admin1/userview')

def deleteseller(request):
    idno=request.GET.get("idn")
    obj=venderreg_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect('/admin1/sellerview')

def fullrentorder(request):
    objec=rent_tbl.objects.all()
    return render(request,'fullrent.html',{"datasse":objec})


def sample1(request):
    return render(request,'sample.html')

def edits(request):
    idno=request.GET.get('idn')
    obj=reg_tbl.objects.filter(id=idno)
    return render(request,'edituser.html',{'secdata':obj})

def updates(request):
    if request.method=="POST":
        idn=request.POST.get("idno")
        uname=request.POST.get("uname")
        umobile=request.POST.get("umobile")
        uemail=request.POST.get("uemail")
        upassword=request.POST.get("upassword")
        reg_tbl.objects.filter(id=idn).update(fnm=uname,mob=umobile,eml=uemail,psw=upassword)
        return redirect("admin1:userview")
    return render(request,'edituser.html')

def selleredits(request):
    idno=request.GET.get('idn')
    obj=venderreg_tbl.objects.filter(id=idno)
    return render(request,'editseller.html',{'secdatas':obj})

def sellerupdates(request):
    if request.method=="POST":
        idn=request.POST.get("idno")
        uname=request.POST.get("uname")
        umobile=request.POST.get("umobile")
        uemail=request.POST.get("uemail")
        upassword=request.POST.get("upassword")
        venderreg_tbl.objects.filter(id=idn).update(fnm=uname,mob=umobile,eml=uemail,psw=upassword)
        return redirect("admin1:sellerview")
    return render(request,'editseller.html')

def selleradd(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        umobile=request.POST.get("umobile")
        uemail=request.POST.get("uemail")
        upassword=request.POST.get("upassword")
        obj=venderreg_tbl.objects.create(fnm=uname,mob=umobile,eml=uemail,psw=upassword)
        obj.save()
        if obj:
            return redirect('admin1:sellerview')

    return render(request,'selleradd.html')

def productview(request):
    obj=product_tbl.objects.all()
    return render(request,'productlist.html',{'pdata':obj})

def deleteitem(request):
    idno=request.GET.get("idn")
    obj=product_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect('/admin1/productview')

def deleterent(request):
    idno=request.GET.get("idn")
    obj=rent_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect('/admin1/fullrentorder')

def deletes(request):
    idno=request.GET.get("idn")
    obj=order_tbl.objects.filter(id=idno)
    obj.delete()
    
    return redirect("/orders")

def fulltransactions(request):
    objec=order_payment.objects.all()
    return render(request,'transactions.html',{"datasse":objec})
