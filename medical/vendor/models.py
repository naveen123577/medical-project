from django.db import models

# Create your models here.
class venderreg_tbl(models.Model):
    fnm=models.CharField(max_length=25)
    mob=models.IntegerField()
    eml=models.EmailField()
    psw=models.CharField(max_length=25)
    def __str__(self):
        return self.fnm
