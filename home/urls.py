from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header = "Jay Electronice"
admin.site.site_title = "Jay Electronice"
admin.site.index_title = "Welcome to Jay Electronice"


urlpatterns = [
  path("", views.index, name='home'),
  path("about/", views.about, name='about'),
  path("services/", views.services, name='services'),
  path("contect/", views.contect, name='contect')

]