from django.contrib import admin
from django.urls import path
from main.views import index,login1,reg,error,payment,orders,logout1,rentdate,rentorder,rentpayment,specificorders,feedback,search,deleteuserorder,deleteuserrent

app_name='medical'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='index'),
    path('', login1,name='userlogin'),
    path('reg/', reg,name='reg'),
    # path('adminindex/', adminindex,name='adminindex'),
    path('error/', error),
    path('payment/', payment,name='payment'),
    path('orders/', orders,name='orders'),
    path('deleteuserorder/', deleteuserorder,name='deleteuserorder'),
    path('deleteuserrent/', deleteuserrent,name='deleteuserrent'),

    path('', logout1,name='logout1'),
    path ('rentdate/',rentdate,name="rentdate"),
    path ('rentorder/',rentorder,name="rentorder"),
    path ('rentpayment/',rentpayment,name="rentpayment"),
    path ('specificorder/',specificorders,name="specificorder"),
    path ('feedback/',feedback,name="feedback"),
    path ('search/',search,name="search"),

]
