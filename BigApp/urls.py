from django.urls import path
from BigApp import views

urlpatterns = [
    path('',views.intro_page,name="Home"),
    path('Shop/',views.shop_page,name="Shop"),
    path('Contact/',views.contact_page,name="Contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('profilter/<cat_name>/',views.profilter,name="profilter"),
    path('single_page/<int:pro_id>/',views.single_page,name="single_page"),
    path('loginsign_page/',views.loginsign_page,name="loginsign_page"),
    path('save_page/',views.save_page,name="save_page"),
    path('loginSignup/',views.loginSignup,name="loginSignup"),
    path('register_logout/',views.register_logout,name="register_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_cart/<int:pro_id>/',views.delete_cart,name="delete_cart"),
    path('user_login_page/',views.user_login_page,name="user_login_page")

]