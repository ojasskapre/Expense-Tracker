from django.contrib import admin
from django.urls import path, re_path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name= 'home'),
    path('expense_detail/<slug:name>/', views.expense_detail, name= 'expense_detail'),
    path('add_detail', views.add_detail, name= 'add_detail'),
    path('delete_detail/<int:id>/', views.delete_detail, name= 'delete_detail'),
]
