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

#Django
from django.contrib import admin
from django.http import HttpResponse
from mindbotslab import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

#App
#from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Prueba
    path('',views.hello_world, name="hi" ),

    #Users
    path('', include(('users.urls', 'users'), namespace='users')),


    #People
    path('people/', include(('people.urls', 'people'), namespace='people')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
