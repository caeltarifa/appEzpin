"""appEzpin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls import url, include

from django.urls import path, include
from django.contrib import admin

from appEzpin.views import view_clasificar_usuario_login
from appEzpin.views import view_pagina_principal

urlpatterns = [
    path('', view_clasificar_usuario_login, name='view_clasificar_usuario_login'),
    path('', view_pagina_principal, name='view_pagina_principal'),
    path('admin/', admin.site.urls),
]



# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]