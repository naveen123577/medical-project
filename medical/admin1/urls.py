from django.contrib import admin
from django.urls import path
from admin1.views import adminindex,userview,sample1,deleteuser,fullrentorder,sellerview,deleteseller,edits,updates,selleredits,sellerupdates,selleradd,productview,deleteitem,deleterent,deletes,fulltransactions
app_name='admin1'
urlpatterns = [
    path('adminindex/', adminindex,name='adminindex'),
    path('', sample1,name='sample1'),
    path('userview', userview,name='userview'),
    # path('adminorders', adminorders,name='adminorders'),
    path('deleteuser', deleteuser,name='deleteuser'),
    path('fullrentorder', fullrentorder,name='fullrentorder'),
    path('sellerview', sellerview,name='sellerview'),
    path('deleteseller', deleteseller,name='deleteseller'),
    path('edituser', edits,name='edituser'),
    path('update', updates, name='updates'),  
    path('editseller', selleredits,name='editseller'),
    path('updateseller', sellerupdates, name='updateseller'),  
    path('selleradd', selleradd, name='selleradd'),  
    path('productview', productview, name='productview'),  
    path('productview', productview, name='productview'),  
    path('deleteitem', deleteitem, name='deleteitem'),  
    path('deleterent', deleterent, name='deleterent'),  
    path('deletes', deletes, name='deletes'),
    path('transactions', fulltransactions, name='transactions'),    

]
