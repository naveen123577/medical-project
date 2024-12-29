from django.shortcuts import render,redirect
from main.models import product_tbl,order_tbl,rent_tbl
from django.http import HttpResponse
# Create your views here.
def vendorindex(request):
    name = request.session.get('nam', 'DefaultName')
    return render(request,'vendordash.html')

from django.core.files.storage import FileSystemStorage

def productadd(request):
    if request.method == "POST":
        pname = request.POST.get("pname1")
        pamount = request.POST.get("pprice1")
        prent = request.POST.get("prent1")
        pseller = request.session.get('nams', 'DefaultName')
        pdes = request.POST.get("pdes1")
        quant=request.POST.get("quantity")
        
        # Handle file upload
        if request.FILES.get("pimage1"):
            pimage = request.FILES["pimage1"]
            fs = FileSystemStorage()
            filename = fs.save(pimage.name, pimage)
            uploaded_file_url = fs.url(filename)
            # Now you can use 'uploaded_file_url' to store in the database if needed
            # But usually, you would store 'filename' to refer to it in your application
            
            product_tbl.objects.create(pnm=pname, pim=filename, prc=pamount, des=pdes, seller=pseller, rentprice=prent,quantity=quant)
        else:
            # Handle case where no image is uploaded if that's valid for your application
            product_tbl.objects.create(pnm=pname, prc=pamount, des=pdes, seller=pseller, rentprice=prent)
        
        return render(request, "vendordash.html")

    return render(request, 'productadd.html')

def sellerorders(request):
    pseller = request.session.get('nams', 'DefaultName')
    print(pseller)
    objec=order_tbl.objects.filter(oseller=pseller)
    return render(request,'sellerorder.html',{"sdatas":objec})

def sellerrent(request):
    pseller1 = request.session.get('nams', 'DefaultName')
    names=request.session['nam']
    objec=rent_tbl.objects.filter(oseller=pseller1)
    return render(request,'sellerrent.html',{"datasses":objec})

def manageitems(request):
    pseller = request.session.get('nams', 'DefaultName')
    objec=product_tbl.objects.filter(seller=pseller)
    return render(request,'manageitems.html',{"sdatas":objec})

def deleteselleritem(request):
    idno=request.GET.get("idn")
    obj=product_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect('/vendor/manageitems')

def deletesellerorder(request):
    idno=request.GET.get("idn")
    obj=order_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect('/vendor/sellerorder')

def deletesellerrent(request):
    idno=request.GET.get("idn")
    obj=rent_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect('/vendor/sellerrent')

def editproduct(request):
    idno=request.GET.get('idn')
    obj=product_tbl.objects.filter(id=idno)
    return render(request,'editproduct.html',{'secdata':obj})

def updateproduct(request):
    if request.method=="POST":
        idn=request.POST.get("idno")
        pname=request.POST.get("pname")
        pprice=request.POST.get("pprice")
        pdes=request.POST.get("pdes")
        pseller=request.POST.get("pseller")
        prent=request.POST.get("prent")
        quant=request.POST.get("quantiti")

        if request.FILES.get("pimage1"):
            pimage = request.FILES["pimage1"]
            fs = FileSystemStorage()
            filename = fs.save(pimage.name, pimage)
            uploaded_file_url = fs.url(filename)
            # Now you can use 'uploaded_file_url' to store in the database if needed
            # But usually, you would store 'filename' to refer to it in your application
            product_tbl.objects.filter(id=idn).update(pnm=pname, pim=filename, prc=pprice, des=pdes, seller=pseller, rentprice=prent, quantity=quant)

            # product_tbl.objects.create(pnm=pname, pim=filename, prc=pprice, des=pdes, seller=pseller, rentprice=prent)
        else:
            # Handle case where no image is uploaded if that's valid for your application
            product_tbl.objects.filter(id=idn).update(pnm=pname, prc=pprice, des=pdes, seller=pseller, rentprice=prent, quantity=quant)
        
        return redirect("vendor:manageitems")
    return render(request,'editproduct.html')
