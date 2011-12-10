from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('ajax.views',
	url(r'^ajax$', 'ajax_mgm', name='ajax_mgm'),
)
