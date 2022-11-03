from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('add/', views.add, name='add'),

]