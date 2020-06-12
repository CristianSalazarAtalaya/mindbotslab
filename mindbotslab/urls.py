"""mindbotslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
""" modulo de URLS de MINDBOTSLAB"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from mindbotslab import views

#App
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Prueba
    path('',views.hello_world, name="hi" ),

    #Users
    path('login', users_views.login_view , name="login"),
    path('logout', users_views.logout_view , name="logout"),

]
