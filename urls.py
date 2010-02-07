from django.conf.urls.defaults import *
from Azul.views import home
from Azul.pictures.views import pictures_home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^azul/', include('azul.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
 #   (r'^admin/', include(admin.site.urls)),
    ('^$', home),
    ('^pictures/$', pictures_home),
)
