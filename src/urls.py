"""FoodAssitant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from FoodAssitant import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^register/$',views.register),
    url(r'success/register/$',views.successregister),
    url(r'^account/register/$',views.create_user),
    url(r'^accounts/auth/$',views.user_auth),
    url(r'^food/',views.add_food),
    url(r'^foodhistory/',views.food_history),
    url(r'^user/',views.user_auth),
    url(r'^foodprefrence/',views.food_prefrence),
    url(r'^addbucket/',views.add_bucket)
   # url(r'^getuser/(?P<pk>[0-9]+)/$',views.user_detail),

]
