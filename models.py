from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class RegisterModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    number=models.IntegerField()
    img=models.ImageField(upload_to='image/',null=True)
    Join_Date=models.DateField(auto_now_add=True)

class CategoryModel(models.Model):
    Category_Name=models.CharField(max_length=70)

class SubCategoryModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)

    SubCategory_Name=models.CharField(max_length=70)

class ProductModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    SubCategory=models.ForeignKey(SubCategoryModel,on_delete=models.CASCADE,null=True)
    Product_Name=models.CharField(max_length=70) 
    Product_Discription=models.CharField(max_length=70)   
    Product_Price=models.IntegerField() 
    Product_Img=models.ImageField(upload_to='image/',null=True)

class CartModel(models.Model):
    Customer=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    Product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)     

class OrderModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    SubCategory=models.ForeignKey(SubCategoryModel,on_delete=models.CASCADE,null=True)
    
    Customer=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    Product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
 
    
    
    


   
    

