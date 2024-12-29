from django.shortcuts import render,redirect
from .models import product_tbl,reg_tbl,adminreg_tbl,order_tbl,rent_tbl,order_payment
from vendor.models import venderreg_tbl
# Create your views here.
def index(request):

    obj=product_tbl.objects.all()
    for y in obj:
        if y.quantity==0:
            msg="Out Of Stock"
            return render(request,'index.html',{'data':obj, 'data2':msg})

    return render(request,'index.html',{'data':obj})
    

from django.contrib.auth import authenticate, login, logout

def login1(request):
        if request.method == 'POST':
            admin_error_msg = None
            email = request.POST.get('em')
            passw = request.POST.get('ps')
            user_obj = reg_tbl.objects.filter(eml=email, psw=passw)
            for m in user_obj:
                nam=m.fnm
                request.session['nam']=nam

            if user_obj:
                return redirect("medical:index")
            admin_obj = adminreg_tbl.objects.filter(aeml=email, apsw=passw)

            if admin_obj:
                return redirect("admin1:adminindex")
            vendorobj=venderreg_tbl.objects.filter(eml=email, psw=passw)
            for m in vendorobj:
                nams=m.fnm
                request.session['nams']=nams

            if vendorobj:
                return redirect("vendor:vendorindex")
            else:
                admin_error_msg = "Invalid Login"
                return render(request,"userlogin.html",{'error':admin_error_msg})

        return render(request, 'userlogin.html')



# Create your views here.


def reg(request):
    if request.method=="POST":
        fname=request.POST.get('fn')
        mobile=request.POST.get('mb')
        email=request.POST.get('em')
        passw=request.POST.get('ps')
        obj=reg_tbl.objects.create(fnm=fname,mob=mobile,eml=email,psw=passw)
        obj.save()
        if obj:
            return redirect('medical:userlogin')

    return render(request,'register.html')

def error(request):
    return render(request,"error.html")

def payment(request):
    idno=request.GET.get('idn')
    name=request.session['nam']
    if request.method == "POST":
        nam=request.POST.get("name")
        hnam=request.POST.get("hname")
        streets=request.POST.get("street")
        pinco=request.POST.get("pincode")
        cit=request.POST.get("city")
        mobi=request.POST.get("mob")

        obj=product_tbl.objects.filter(id=idno)
        for m in obj:
            pn = m.pnm  # Use dot notation to access attributes
            pr = m.prc
            ds = m.des
            se = m.seller
        if obj:               
            ob1=order_tbl.objects.create(opnm=pn,oprc=pr,odes=ds,oseller=se,Buyer=name)
            ob1.save()
            ob2=order_payment.objects.create(name=nam,hname=hnam,street=streets,pincode=pinco,city=cit,mobile=mobi,item=pn,price=pr,buyer=name)
            ob2.save()


        if ob1:
            for m in obj:
                quant=m.quantity-1
                product_tbl.objects.filter(id=idno).update(quantity=quant)
                objec=order_tbl.objects.filter(Buyer=name)

                return render(request,'orders.html',{"odatass":objec})


    request.session['id']=idno

    return render(request,'payment.html')

def orders(request):
    objec=order_tbl.objects.all()
    return render(request,'fullorders.html',{"datas":objec})


def specificorders(request):
    name=request.session['nam']
    objec=order_tbl.objects.filter(Buyer=name)
    return render(request,'orders.html',{"odatass":objec})



def deleteuserorder(request):
    idno=request.GET.get("idn")
    obj=order_tbl.objects.filter(id=idno)
    obj.delete()   
    return redirect("/specificorder")

def deleteuserrent(request):
    idno=request.GET.get("idn")
    obj=rent_tbl.objects.filter(id=idno)
    obj.delete()   
    return redirect("/rentorder")

def logout1(request):
    logout(request)
    return render(request,'userview.html')


from datetime import datetime
from datetime import datetime
from django.shortcuts import render
from .models import product_tbl, rent_tbl  # Ensure you have these models defined somewhere in your Django app

def rentdate(request):
    if request.method == 'POST':
        duration = int(request.POST.get('duration', 0))  # Get duration and convert to integer, defaulting to 0 if not found
        request.session['du'] = duration
        idno1 = request.GET.get('ids')
        request.session['ids'] = idno1
        name = request.session.get('nam', '')  # Assuming 'nam' is previously set in the session

        # Assuming you want to save the current date and time as the submission date
        submission_date = datetime.now()

        # Calculate the amount based on duration
        # Base amount is 10 for duration = 1, and increases by 5 for each additional unit of duration
        if duration >= 1:
            amount = 10 + (duration - 1) * 5
        else:
            amount = 0  # Or handle invalid duration differently

        # Fetch the product details
        obj = product_tbl.objects.filter(id=idno1)  # Assuming idno1 uniquely identifies a product, so we use first() to get the object
        for m in obj:
            pn = m.pnm  # Use dot notation to access attributes directly
            ds = m.des
            se = m.seller
        if obj:               
            ob1=rent_tbl.objects.create(opnm=pn, odes=ds, oseller=se, Buyer=name, oduration=duration, odate=submission_date, oamount=amount)
            ob1.save()

        if ob1:
            for m in obj:
                quant=m.quantity-1
                product_tbl.objects.filter(id=idno1).update(quantity=quant)


            # Create a new rent_tbl entry

        return redirect('medical:rentpayment')
    else:
        return render(request, "rentdate.html")

def rentorder(request):
    duration=request.session['du']
    idno2=request.session['ids']
    names=request.session['nam']
    idno2=request.session['ids']
    submission_date = datetime.now()
    objec=rent_tbl.objects.filter(Buyer=names)
    return render(request,'rentorders.html',{"datasse":objec})

def rentpayment(request):
    name=request.session.get('nam', '')
    idno1=request.session['ids']
    print(name,idno1)
    if request.method == "POST":
        nam=request.POST.get("name")
        hnam=request.POST.get("hname")
        streets=request.POST.get("street")
        pinco=request.POST.get("pincode")
        cit=request.POST.get("city")
        mobi=request.POST.get("mob")

        obj = product_tbl.objects.filter(id=idno1)  # Assuming idno1 uniquely identifies a product, so we use first() to get the object
        for m in obj:
            pn = m.pnm  # Use dot notation to access attributes
            pr = m.prc
            ds = m.des
            se = m.seller



    # print(idno)
        if obj:               
            ob2=order_payment.objects.create(name=nam,hname=hnam,street=streets,pincode=pinco,city=cit,mobile=mobi,item=pn,price=pr,buyer=name)
            ob2.save()
            objec=rent_tbl.objects.filter(Buyer=name)

            return render(request,'rentorders.html',{"datasse":objec})


    return render(request,'payment.html')


from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def feedback(request):
    if request.method == "POST":
        # Get form data
        name = request.session['nam']
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Set your default "To" address here
        to_email = 'naveensibi355@gmail.com'

        # Compose the email message with name, phone number, and from_email
        full_message = f"Name: {name}\n\n{message}"

        # Send email
        send_mail(subject, full_message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)

        # Display success message
        messages.success(request, "Mail sent successfully...")

    return render(request, "feedback.html")

def search(request):
    if request.method == 'POST':
        search2 = request.POST.get('search1')
        obj = product_tbl.objects.filter(pnm=search2)

        if obj:
            return render(request, 'index2.html', {'data2': obj})
        else:
            return render(request, 'index.html')
    else:
        return render(request,'index.html')
