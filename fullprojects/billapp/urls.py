from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.home_view,name='home'),
    path('addcustomer/',views.addcustomer,name='addcustomer'),
    path('customer/',views.customerlist,name='customerlist'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('products/',views.productlist,name='productlist'),
    path('invoice/',views.invoice,name='invoice'),
    path('products/',views.productlist,name='productlist'),
    path('invoices/',views.invoicelist,name='invoicelist'),
    path('',views.dashboard,name='dashboard'),
   
]