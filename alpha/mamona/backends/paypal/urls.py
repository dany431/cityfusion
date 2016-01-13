from django.conf.urls import *

urlpatterns = patterns('mamona.backends.paypal.views',
	url(r'^return/(?P<order_class>\w+)/(?P<payment_id>[0-9]+)/$', 'return_from_gw', name='mamona-paypal-return'),
	url(r'^ipn/(?P<order_class>\w+)/$', 'ipn', name='mamona-paypal-ipn'),
)
