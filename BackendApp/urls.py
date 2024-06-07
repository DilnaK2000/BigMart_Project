from django.urls import path
from BackendApp import views

urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),
    path('display_page/',views.display_page,name="display_page"),
    path('imgsave_page/',views.imgsave_page,name="imgsave_page"),
    path('table_page/',views.table_page,name="table_page"),
    path('edit_page/<int:pro_id>/',views.edit_page,name="edit_page"),
    path('update_img/<int:pro_id>/',views.update_img,name="update_img"),
    path('delete_img/<int:pro_id>/',views.delete_img,name="delete_img"),
    path('login_page/',views.login_page,name="login_page"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admlogout/',views.admlogout,name="admlogout"),
    path('product_page/',views.product_page,name="product_page"),
    path('productsave/',views.productsave,name="productsave"),
    path('view_prod/', views.view_prod, name="view_prod"),
    path('proedit/<int:pro_id>/',views.proedit,name="proedit"),
    path('update_save/<int:pro_id>/',views.update_save,name="update_save"),
    path('delete_page/<int:pro_id>/',views.delete_page,name="delete_page"),
    path('ContDetails/',views.ContDetails,name="ContDetails"),
    path('contact_delete/<int:pro_id>/',views.contact_delete,name="contact_delete")
]