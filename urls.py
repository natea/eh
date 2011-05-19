from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^eh/', include('eh.foo.urls')),
    (r'^%s/*' % settings.FURL_ROOT, include('eh.furl.urls'))
)


urlpatterns += patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/furl'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)))
    
    
urlpatterns += staticfiles_urlpatterns()