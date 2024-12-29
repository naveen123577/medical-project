from django.db import models

# Create your models here.
class product_tbl(models.Model):
    pnm=models.CharField(max_length=25)
    pim=models.FileField(upload_to='pic')
    prc=models.IntegerField()
    des=models.TextField()
    seller=models.CharField(max_length=25)
    rentprice=models.IntegerField()
    quantity=models.IntegerField()
    def __str__(self):
        return self.pnm


class adminreg_tbl(models.Model):
    afnm=models.CharField(max_length=25)
    amob=models.IntegerField()
    aeml=models.EmailField()
    apsw=models.CharField(max_length=25)
    def __str__(self):
        return self.afnm


class reg_tbl(models.Model):
    fnm=models.CharField(max_length=25)
    mob=models.IntegerField()
    eml=models.EmailField()
    psw=models.CharField(max_length=25)
    def __str__(self):
        return self.fnm
    

class order_tbl(models.Model):
    opnm=models.CharField(max_length=225)
    Buyer=models.CharField(max_length=25,default='user')
    # pim=models.FileField(upload_to='pic')
    oprc=models.IntegerField()
    odes=models.TextField()
    oseller=models.CharField(max_length=225)
    def __str__(self):
        return self.opnm

class rent_tbl(models.Model):
    opnm=models.CharField(max_length=225)
    Buyer=models.CharField(max_length=25,default='user')
    # pim=models.FileField(upload_to='pic')
    # orentprice=models.IntegerField()
    odes=models.TextField()
    oseller=models.CharField(max_length=225)
    odate=models.DateField(auto_now_add=True)
    oduration=models.IntegerField()
    oamount=models.IntegerField()
    def __str__(self):
        return self.opnm

class order_payment(models.Model):
    name=models.CharField(max_length=200)
    hname=models.CharField(max_length=400)
    street=models.CharField(max_length=400)
    pincode=models.CharField(max_length=300)
    city=models.CharField(max_length=300)
    mobile=models.IntegerField()
    item=models.CharField(max_length=200,default="sample")
    price=models.IntegerField(default=20)
    buyer=models.CharField(max_length=200,default="demo")
    def __str__(self):
        return self.name
