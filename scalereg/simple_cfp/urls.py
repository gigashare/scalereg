from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'scalereg.simple_cfp.views.index'),
    (r'^speaker_registration/$', 'scalereg.simple_cfp.views.RegisterSpeaker'),
)