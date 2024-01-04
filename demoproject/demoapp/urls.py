from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index')
    # path('', views.home, name='home'),
    # path('calculate/', views.calculate, name='calculate'),
    # path('contact/', views.contact, name='contact'),
    # path('details/', views.details, name='details'),
    # path('thanks/', views.thanks, name='thanks'),
]