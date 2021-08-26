from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('dologin/',views.dologin, name='dologin'),
    path('register/',views.register, name='register'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path("contact/", views.contact_form, name="contact_form"),
]