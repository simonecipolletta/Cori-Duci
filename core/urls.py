"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # LE API DEVONO STARE PRIMA DEL CATCH-ALL
    path('api/', include('products.urls')),
    path('api/contatti/', include('contacts.urls')),
]
# Aggiungi questa parte per servire i file multimediali durante lo sviluppo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# AGGIUNGI QUESTO BLOCCO ALLA FINE DEL FILE:
# Forza Django a servire i file Media anche con DEBUG=False
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

# 3. CATCH-ALL (DEVE STARE TASSATIVAMENTE ALLA FINE)
urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]