from django.shortcuts import render,redirect
from .models import Customer,Product,Invoice
from .forms import CustomerForm,ProductForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')
@login_required
def addcustomer(request):
    if request.method=='POST':
       form = CustomerForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('customerlist')
    else:
        form = CustomerForm()
    return render(request,'addcustomer.html',{'form':form})
def customerlist(request):
    customers= Customer.objects.all()
    return render(request,'customerlist.html',{'customers':customers })

def addproduct(request):
   if  request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productlist')
   else:
        form = ProductForm()
                  
   return render(request,'addproduct.html',{'form':form})     
   
def productlist(request):
    products=Product.objects.all()
    return render(request,'productlist.html',{'products':products})
def invoice(request):
    
    if request.method == 'POST':
        customer_id =request.POST.get('customer')
        Product_id=request.POST.get('product')
        quantity=int(request.POST.get('quantity') or 1) 

        selected_customer=Customer.objects.get(id=customer_id)
        selected_product=Product.objects.get(id=Product_id)

        totalamount = selected_product.price*quantity  
        
        Invoice.objects.create(customer=selected_customer,product=selected_product,quantity=quantity,totalamount=totalamount) 


        

        selected_product.stock -= quantity
        selected_product.save()


        return redirect('invoicelist')

    customers = Customer.objects.all()
    products =Product.objects.all()
        
    
    return render(request,'invoice.html',{
      'customers':customers,
      'products':products })


def invoicelist(request):
   invoices=Invoice.objects.all()
   return render(request,'invoicelist.html',{'invoices':invoices})# Create your views here.
def home_view(request):
    return render(request,'home.html')
def dashboard(request):
    total_products=Product.objects.count()
    total_stock=Product.objects.aggregate(total=sum('stock'))['total'] or 0
    context={
        'total_products':total_products,
        'total_stock':total_stock,
    }
    return render(request,'dashboard.html',context)