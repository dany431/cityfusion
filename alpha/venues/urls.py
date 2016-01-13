from django.conf.urls import patterns, url
from venues import views

urlpatterns = patterns('',
    url(r'^$',
        views.venues,
        name='venues'
    ),
    url(r'^venue-tags/$',
        views.venue_tags,
        name="venue_tags"
    ),
    url(r'^venue-account-tags/(?P<venue_account_id>\d+)$',
        views.venue_account_tags,
        name="venue_account_tags"
    ),
    url(r'^private/(?P<slug>[-\w]+)/$',
        views.private_venue_account,
        name='private_venue_account'
    ),
    url(r'^edit/(?P<slug>[-\w]+)/$',
        views.edit_venue_account,
        name='edit_venue_account'
    ),
    url(r'^venue-create/$',
        views.create_venue_account,
        name='create_venue_account'
    ),
    url(r'venue-already-in-use/(?P<venue_account_id>\d+)/$',
        views.venue_account_already_in_use,
        name="venue_account_already_in_use"
    ),
    url(r'^set-venue-privacy/(?P<venue_account_id>[\d]+)/(?P<privacy>(public|private))/$',
        views.set_venue_privacy,
        name='save_venue_privacy'
    ),
    url(r'^unlink-venue-account/$',
        views.unlink_venue_account_from_user_profile,
        name="unlink_venue_account_from_user_profile"
    ),
    url(r'^unlink-venue-account-admin/(?P<slug>[-\w]+)/$',
        views.unlink_venue_account_by_admin,
        name="unlink_venue_account_by_admin"
    ),
    url(r'^(?P<slug>[-\w]+)/$',
        views.public_venue_account,
        name='public_venue_account'
    ),
    url(r'location/edit/(?P<venue_id>\d+)/$',
        views.edit_venue,
        name='edit_venue'),

    url(r'location/remove/(?P<venue_id>\d+)/$',
        views.remove_venue,
        name='remove_venue')
)