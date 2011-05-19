from django.conf.urls.defaults import *


urlpatterns = patterns('eh.furl.views',
    # Example:
    (r'^$', 'index'),
    (r'^add$', 'add_link'),
    (r'^adder$', 'send_adder'),
    (r'^tags$', 'tags'),
    (r'^tag/(?P<tag>\w+?)$', 'get_tag'),
    (r'^extras$', 'extras'),
    
)
