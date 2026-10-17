from django.db import models
class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone= models.CharField(max_length=15)
    email=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    name =models.CharField(max_length=100)
    price= models.DecimalField(max_digits=  10,decimal_places=2)
    stock=models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
   
   
           

class Invoice(models.Model):
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE) 
    product=models.ForeignKey('product',on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(default=1)
    date=models.DateTimeField(auto_now_add=True)
    totalamount=models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"Invoice #{self.id}_{self.customer.name}_{self.quantity}_{self.totalamount}"
    def save(self,*args,**kwargs):
        
            self.totalamount=self.product.price*self.quantity
            self.product.stock -= self.quantity
            self.product.save()
            super().save(*args,**kwargs)     