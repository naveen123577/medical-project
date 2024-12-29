from django.contrib import admin
from .models import product_tbl,adminreg_tbl,reg_tbl,order_tbl,rent_tbl
# Register your models here.
admin.site.register(product_tbl),
admin.site.register(reg_tbl),
admin.site.register(adminreg_tbl),
admin.site.register(order_tbl),
admin.site.register(rent_tbl),