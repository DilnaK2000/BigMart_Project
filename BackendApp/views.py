from django.shortcuts import render,redirect
from BackendApp.models import bigdb,Productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from BigApp.models import biginput_db
from django.contrib import messages

# Create your views here.

def index_page(ind):
    return render(ind,"index.html")
def display_page(dis):
    return render(dis,"display.html")
def imgsave_page(dis):
    if dis.method=="POST":
        cn = dis.POST.get('Cname')
        de = dis.POST.get('Description')
        im = dis.FILES['Image']
        obj=bigdb(CatName=cn,Description=de,img=im)
        obj.save()
        messages.success(dis,'Category Saved Successfully..')
        return redirect(display_page)
def table_page(dis):
    data = bigdb.objects.all()
    return render(dis,"table.html",{'data':data})
def edit_page(dis,pro_id):
    data = bigdb.objects.get(id=pro_id)
    messages.warning(dis,'Edit Your Mistakes..')
    return render(dis,"edit.html",{'data':data})
def update_img(request,pro_id):
    if request.method=="POST":
        cn = request.POST.get('Cname')
        de = request.POST.get('Description')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = bigdb.objects.get(id=pro_id).img
        bigdb.objects.filter(id=pro_id).update(CatName=cn,Description=de,img=file)
        return redirect(table_page)

def delete_img(request,pro_id):
    x=bigdb.objects.filter(id=pro_id)
    x.delete()
    messages.error(request,'Warning')
    return redirect(table_page)
def login_page(log):
    return render(log,"Login.html")
def adminlogin(request):
    if request.method=="POST":
        un= request.POST.get('username')
        pwd= request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,'Welcome..')
                return redirect(index_page)
            else:
                messages.error(request, 'Default Password..')
                return redirect(login_page)
        else:
            messages.warning(request, 'Default Username..')
            return redirect(login_page)
def admlogout(request):
    del  request.session['username']
    del request.session['password']
    return redirect(login_page)
def product_page(req):
    data = bigdb.objects.all()
    return render(req,"product.html",{'data':data})
def productsave(dis):
    if dis.method=="POST":
        cn = dis.POST.get('Caname')
        pn=dis.POST.get('prname')
        de = dis.POST.get('Desc')
        p = dis.POST.get('pname')
        im = dis.FILES['Image']
        obj=Productdb(category_name=cn,product_name=pn,Des=de,pp=p,img=im)
        obj.save()
        messages.success(dis,'Product Saved Successfully..')
        return redirect(product_page)
def view_prod(req):
    data = Productdb.objects.all()
    return render(req,"View_product.html", {'data':data})
def proedit(request,pro_id):
    cat = Productdb.objects.get(id=pro_id)
    pro = bigdb.objects.all()
    return render(request,"pro_edit.html",{'cat':cat , 'pro':pro})

def update_save(request,pro_id):
    if request.method=="POST":
        c = request.POST.get('Caname')
        pi = request.POST.get('prname')
        d = request.POST.get('Desc')
        p = request.POST.get('pname')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=pro_id).img
        Productdb.objects.filter(id=pro_id).update(category_name=c,product_name=pi,Des=d,pp=p,img=file)
        return redirect(view_prod)

def delete_page(de,pro_id):
    x = Productdb.objects.filter(id=pro_id)
    x.delete()
    messages.error(de,'Warning')
    return redirect(view_prod)
def ContDetails(request):
    data = biginput_db.objects.all()
    return render(request,"Contact_details.html",{'data':data})
def contact_delete(request,pro_id):
    x= biginput_db.objects.filter(id=pro_id)
    x.delete()
    messages.error(request,'Delete...')
    return redirect(ContDetails)











