from django.contrib import admin
from django.urls import path
from vendor.views import vendorindex,productadd,sellerorders,sellerrent,manageitems,deleteselleritem,editproduct,updateproduct,deletesellerorder,deletesellerrent
from django.conf import settings
from django.conf.urls.static import static
app_name='vendor'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendordash/',vendorindex,name='vendorindex'),
    path('productadd/',productadd,name='productadd'),
    path('sellerorder/',sellerorders,name='sellerorder'),
    path('sellerrent/',sellerrent,name='sellerrent'),
    path('manageitems/',manageitems,name='manageitems'),
    path('deleteselleritem/',deleteselleritem,name='deleteselleritem'),
    path('editproduct/',editproduct,name='editproduct'),
    path('updateproduct/',updateproduct,name='updateproduct'),
    path('deletesellerorder/',deletesellerorder,name='deletesellerorder'),
    path('deletesellerrent/',deletesellerrent,name='deletesellerrent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
