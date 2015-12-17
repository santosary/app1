from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', include('compras.urls')),
    url(r'^CCB/', include('compras.urls')),
    url(r'^ccb/', include('compras.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^loginadmin123siteccb/', include(admin.site.urls)),
)# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

