from django.conf.urls.defaults import *
from views import documentation

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/?$', documentation, name='api-documentation'),
)
