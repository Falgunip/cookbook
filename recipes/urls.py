from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:recipe_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('save/', views.save, name='save'),
]

