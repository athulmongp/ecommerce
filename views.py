from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import*
from django.contrib.auth.decorators import login_required

def homepage(request):
    data=CategoryModel.objects.all()
    return render(request,"home.html",{'data':data})
def adminhomepage(request):
    data=CategoryModel.objects.all()
    return render(request,"adminhome.html",{'data':data})

def customerhomepage(request):
    data=CategoryModel.objects.all()
    current_user=request.user
    uid=current_user.id
    print(uid)
    customer=RegisterModel.objects.get(user=uid)
    
    return render(request,"customerhome.html",{'data':data,'customer':customer})

def uregpage(request):
    return render(request,"userreg.html")

def registration(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['eid']
        usname=request.POST['uname']
        num=request.POST['ph']
        pswd=request.POST['pass']
        cpswd=request.POST['cpass']
       
        img=request.FILES.get('file')
        

        if pswd==cpswd:
            if User.objects.filter(username=usname).exists():
                print("1")
                return redirect('uregpage')
            elif User.objects.filter(email=email).exists():
                print("2")
                return redirect('uregpage')
            else:
                user=User.objects.create_user(first_name=fn,last_name=ln,email=email,username=usname,password=pswd)
                user.save()
                data=User.objects.get(id=user.id)
                customer=RegisterModel(number=num,img=img,user=data)
                customer.save()
                print("success")
                return redirect('log')

        else:
            print("password error")
            return redirect('uregpage')

    else:
            print(" error")
            return redirect('uregpage')

def log(request):
    return render(request,"login.html") 
def loginpage(request):
    if request.method=='POST':
        username = request.POST['ui']
        password = request.POST['pa']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            if request.user.is_staff==1:
                print("admin")
                
                return redirect('adminhomepage')
                 
            else:
              
              print("chome")
              return redirect('customerhomepage')
              
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            print("try again")
            return redirect('log')
    else:
        print("try again")
        return redirect('log')
    

def categorypage(request):
    return render(request,"maincategory.html")

def addcategory(request):
    if request.method == 'POST':
        category=request.POST['cname']
        data = CategoryModel(Category_Name=category)
        data.save()
        return redirect('adminhomepage')    
    
 

def subcategorypage(request):
    data=CategoryModel.objects.all()
    return render(request,"subcategory.html",{'data':data})

def addsubcategory(request):
    if request.method == 'POST':
        subcategory=request.POST['subcname']
        select=request.POST.get('select')
        category=CategoryModel.objects.get(id=select)
        data =SubCategoryModel(SubCategory_Name=subcategory,Category=category)
        data.save()
        return redirect('adminhomepage') 
    
def productpage(request):  
    data=SubCategoryModel.objects.all()
    return render(request,"product.html",{'data':data})  
def addproduct(request):
    if request.method == 'POST':
        pn=request.POST['prtname']
        pd=request.POST['prtdispription']
        pp=request.POST['prtprice']
        img=request.FILES.get('file')
        select=request.POST.get('select')
        scategory=SubCategoryModel.objects.get(id=select)
        data =ProductModel(Product_Name=pn,Product_Discription=pd,Product_Price=pp,Product_Img=img,SubCategory=scategory,Category=scategory.Category)
        data.save()
        return redirect('adminhomepage')    
    

@login_required(login_url='log')    
def showproductpage(request,did):  

    cate=SubCategoryModel.objects.filter(Category=did)
    data=ProductModel.objects.filter(Category=did)
    
    
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=RegisterModel.objects.get(user=uid)
    return render(request,"showproduct.html",{'data':data,'user':user,'cate':cate})  

def showsubproductpage(request,did):  
    
    sub=CategoryModel(id=did)

    cate=SubCategoryModel.objects.filter(Category=sub.id)
    data=ProductModel.objects.filter(SubCategory=did)
    
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=RegisterModel.objects.get(user=uid)
    return render(request,"subproduct.html",{'data':data,'user':user,'cate':cate})  

def showcustomerpage(request):  
    data=RegisterModel.objects.all()
   
    return render(request,"showcustomer.html",{'data':data})   


def profilepage(request,did):
    user=RegisterModel.objects.get(id=did)
    data=CategoryModel.objects.all()
   
    return render(request,"profile.html",{'user':user,'data':data})



def editcustomerpage(request,did):
    customer=RegisterModel.objects.get(id=did)
    
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=RegisterModel.objects.get(user=uid)
    
    return render(request,'editcustomer.html',{'user':user,'customer':customer})

def edit_customerdetails(request,did):
    if request.method=='POST':
        customer=RegisterModel.objects.get(id=did)
        old=customer.img
        new=request.FILES.get('file')
        if old!=None and new==None:
            customer.img=old
        else:
            customer.img=new
        
        customer.user.first_name=request.POST.get('fname')
        customer.user.last_name=request.POST.get('lname')
        customer.user.email=request.POST.get('eid')
        customer.number=request.POST.get('ph')
        customer.user.username=request.POST.get('uname')
        customer.save()
        customer.user.save()

        print("update success")
        return redirect('profilepage', customer.id )
    print("else")
    return request(request,"editcustomer.html")

def delete_profile(request,did):
    customer=RegisterModel.objects.get(id=did)
    customer.delete()
    print("delete profile")
    return redirect('homepage')

def orderproduct(request,did):
    data=ProductModel.objects.get(id=did)
    ca=CategoryModel.objects.all()
    current_user=request.user
    uid=current_user.id
    user=RegisterModel.objects.get(user=uid)
    return render(request,"order.html",{'data':data,'ca':ca,'user':user})

def buynow(request,did):
    data=ProductModel.objects.get(id=did)
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=RegisterModel.objects.get(user=uid)

    product=OrderModel(Category=data.Category,SubCategory=data.SubCategory,Customer=user,Product=data)
    product.save()
    print("shoping complited")
    return redirect('success')

def success(request):
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=RegisterModel.objects.get(user=uid)
    return render(request,"success.html",{'user':user})

def addcart(request,did):
    data=ProductModel.objects.get(id=did)
    current_user=request.user
    uid=current_user.id
    
    user=RegisterModel.objects.get(user=uid)

    cart=CartModel(Customer=user,Product=data)
    cart.save()
    return redirect('customerhomepage')


def cart(request,did):
    data=CartModel.objects.filter(Customer=did)
    ca=CategoryModel.objects.all()
    
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=RegisterModel.objects.get(user=uid)
    return render(request,"cart.html",{'data':data,'user':user,'ca':ca})

def remove_cart(request,did):
    cart=CartModel.objects.get(id=did)
    cart.delete()
    print("remove cart")
    return redirect('customerhomepage')

def order_details(request):
    data=OrderModel.objects.all()
    
    # current_user=request.user
    # uid=current_user.id
    # user=RegisterModel.objects.get(user=uid)
    return render(request,"order_details.html",{'data':data})

def product_details(request):
    data=ProductModel.objects.all()
    return render(request,"product_details.html",{'data':data})

def editproductpage(request,did):
    product=ProductModel.objects.get(id=did)
    
    data=SubCategoryModel.objects.all()
    
    return render(request,'editproduct.html',{'product':product,'data':data})

def edit_products(request,did):
    if request.method=='POST':
        
        product=ProductModel.objects.get(id=did)
        old=product.Product_Img
        new=request.FILES.get('file')
        if old!=None and new==None:
            product.Product_Img=old
        else:
            product.Product_Img=new
        
        product.Product_Name=request.POST.get('prtname')
        product.Product_Discription=request.POST.get('prtdispription')
        product.Product_Price=request.POST.get('prtprice')
        select=request.POST.get('select')
        scategory=SubCategoryModel.objects.get(id=select)
        product.SubCategory=scategory
        product.Category=scategory.Category
        product.save()
        

        print("update success")
        return redirect('product_details')
    print("else")
    return request(request,"editproduct.html")

# def customer_order(request,did):
#     data=OrderModel.objects.filter(Customer=did)
#     return request(request,"customer_order.html",{'data':data})



def delete_product(request,did):
    product=ProductModel.objects.get(id=did)
    product.delete()
    print("remove cart")
    return redirect('product_details')

def logout(request):
	auth.logout(request)
	return redirect('homepage')