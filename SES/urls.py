"""SES URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from home.forms import ExRegistrationForm
from registration.backends.simple.views import RegistrationView

urlpatterns = [
     url(r'accounts/register/$', 
        RegistrationView.as_view(form_class = ExRegistrationForm), 
        name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^home/', 'home.views.home', name='home'),
    url(r'^GroupProfile/Overview/', 'home.views.GroupProfile', name='GroupProfile'),
    url(r'^GroupProfile/BeginToTrade/', 'home.views.BeginToTrade', name='BeginToTrade'),
    url(r'^GroupProfile/ShowTransactions/', 'home.views.ShowTransactions', name='ShowTransactions'),
    url(r'^admin/', admin.site.urls),
]
