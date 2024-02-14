from shopapp import views
from django.urls import path

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('adminhomepage',views.adminhomepage,name="adminhomepage"),

    path('uregpage',views.uregpage,name="uregpage"),
    path('registration',views.registration,name="registration"),
    path('showcustomerpage',views.showcustomerpage,name="showcustomerpage"),
    path('customerhomepage',views.customerhomepage,name="customerhomepage"),
    path('profilepage/<int:did>',views.profilepage,name="profilepage"),
    path('editcustomerpage/<int:did>',views.editcustomerpage,name="editcustomerpage"),
    path('edit_customerdetails/<int:did>',views.edit_customerdetails,name="edit_customerdetails"),
    path('delete_profile/<int:did>',views.delete_profile,name="delete_profile"),

    path('log',views.log,name="log"),
    path('loginpage',views.loginpage,name="loginpage"),

    path('categorypage',views.categorypage,name="categorypage"),
    path('addcategory',views.addcategory,name="addcategory"),

    path('productpage',views.productpage,name="productpage"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('showproductpage/<int:did>',views.showproductpage,name="showproductpage"),
    path('showsubproductpage/<int:did>',views.showsubproductpage,name="showsubproductpage"),
    path('orderproduct/<int:did>',views.orderproduct,name="orderproduct"),
    path('buynow/<int:did>',views.buynow,name="buynow"),
    path('success',views.success,name="success"),
    path('addcart/<int:did>',views.addcart,name="addcart"),
    path('cart/<int:did>',views.cart,name="cart"),
    path('remove_cart/<int:did>',views.remove_cart,name="remove_cart"),
    # path('customer_order/<int:did>',views.customer_order,name="customer_order"),

    
    path('order_details',views.order_details,name="order_details"),
    path('product_details',views.product_details,name="product_details"),
    path('editproductpage/<int:did>',views.editproductpage,name="editproductpage"),
    path('edit_products/<int:did>',views.edit_products,name="edit_products"),
    path('delete_product/<int:did>',views.delete_product,name="delete_product"),

    path('subcategorypage',views.subcategorypage,name="subcategorypage"),
    path('addsubcategory',views.addsubcategory,name="addsubcategory"),


    path('logout',views.logout,name="logout"),

   
]