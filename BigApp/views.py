from django.shortcuts import render,redirect
from BackendApp.models import Productdb,bigdb
from BigApp.models import biginput_db,logindb,cartdb
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def intro_page(int):
    cat = bigdb.objects.all()
    pro = Productdb.objects.all()
    return render(int,"Home.html",{'cat':cat , 'pr':pro})
def shop_page(sho):
    pro = Productdb.objects.all()
    cat = bigdb.objects.all()
    return render(sho,"Shop.html",{'products':pro , 'cat':cat})
def contact_page(co):
    cat = bigdb.objects.all()
    return render(co,"Contact.html",{'cat':cat})
def save_contact(request):
    if request.method=="POST":
        yn = request.POST.get('yname')
        ya = request.POST.get('yaddress')
        ye = request.POST.get('mail')
        ym = request.POST.get('mess')
        obj=biginput_db(Your_Name=yn,Address=ya,Email=ye,Message=ym)
        obj.save()
        return redirect(contact_page)
def profilter(req,cat_name):
    data = Productdb.objects.filter(category_name=cat_name)
    return render(req,"Pro_Filter.html",{'data':data})
def single_page(co,pro_id):
    data =Productdb.objects.get(id=pro_id)
    return render(co,"single_product.html",{'data':data})
def loginsign_page(log):
    return render(log,"Login_signup.html")
def save_page(r):
    if r.method=="POST":
        u=r.POST.get("user")
        em=r.POST.get("mail")
        pa=r.POST.get("pass1")
        obj=logindb(username=u, Email=em, password=pa)
        if logindb.objects.filter(username=u).exists():
            messages.warning(r,"username already exist...")
            return redirect(loginsign_page)
        elif logindb.objects.filter(Email=em).exists():
            messages.warning(r,"Email id already exist...")
            return redirect(loginsign_page)
        else:
            obj.save()
            messages.success(r, "Registered successfully..")
        return redirect(loginsign_page)
def loginSignup(request):
    if request.method=="POST":
        un= request.POST.get('Uname')
        pwd= request.POST.get('Passw')
        if logindb.objects.filter(username=un , password=pwd).exists():
            messages.success(request, 'Welcome..')
            request.session['username']=un
            request.session['password']=pwd
            return redirect(intro_page)
        else:
            messages.error(request, 'Default Password..')
            return redirect(loginsign_page)
    else:
        messages.error(request, 'Default UserName..')
        return redirect(loginsign_page)

def register_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(intro_page)

def save_cart(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pn = request.POST.get('pname')
        qt = request.POST.get('qtyy')
        tp = request.POST.get('totalprice')
        obj= cartdb(usename=un,proname=pn,quantity=qt,price=tp)
        obj.save()
        return redirect(intro_page)

def cart_page(request):
    data = cartdb.objects.filter(usename=request.session['username'])
    total = 0
    for d in data:
        total = total+d.price
    return render(request,"cart.html", {'data':data , 'total':total})

def delete_cart(request,pro_id):
    x= cartdb.objects.filter(id=pro_id)
    x.delete()
    return redirect(cart_page)
def user_login_page(request):
    return render(request,"userlogin.html")







