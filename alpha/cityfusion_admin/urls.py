from django.conf.urls import patterns, url
from cityfusion_admin import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Home
    url(r'^$', 
        TemplateView.as_view(template_name="cf-admin/home.html"),
        name='cfadmin_home'
    ),

    # Reports
    url(r'^report-event/$', 
        views.report_event,
        name='report_event'
    ),
    url(r'^report-event-list/$', 
        views.report_event_list,
        name='report_event_list'
    ),
    url(r'^report-event-process/(?P<report_id>\d+)/$', 
        views.report_event_process,
        name='report_event_process'
    ),

    # Claims
    url(r'^claim-event/$',
        views.claim_event,
        name='claim_event'
    ),    
    url(r'^claim-event-list/$',
        views.claim_event_list,
        name='claim_event_list'
    ),
    url(r'^transfer-event/(?P<claim_id>\d+)/$',
        views.transfer_event,
        name='transfer_event'
    ),
    url(r'^claim-event-refuse/(?P<claim_id>\d+)/$', 
        views.claim_event_refuse,
        name='claim_event_refuse'
    ),

    #Facebook
    url(r'^import-facebook-events/$',
        views.import_facebook_events,
        name='import_facebook_events'
    ),
    url(r'^load-facebook-events/$',
        views.load_facebook_events,
        name='load_facebook_events'
    ),
    url(r'^reject-facebook-event/$',
        views.reject_facebook_event,
        name='reject_facebook_event'
    ),


    url(r'^locations/$',
        views.location_autocomplete,
        name='admin_location_autocomplete'
    ),

    url(r'^users/$',
        views.user_autocomplete,
        name='admin_user_autocomplete'
    ),

    # Advertising
    url(r'^admin-advertising/$',
        views.admin_advertising,
        name='admin_advertising'
    ),
    # Advertising
    url(r'^admin-expired-advertising/$',
        views.admin_expired_advertising,
        name='admin_expired_advertising'
    ),
    url(r'^admin-advertising/setup/$',
        views.admin_advertising_setup,
        name='admin_advertising_setup'
    ),    
    url(r'^admin-advertising/campaign/(?P<campaign_id>\d+)/edit/$',
        views.admin_advertising_edit_campaign,
        name='admin_advertising_edit_campaign'
    ),
    url(r'^admin-advertising/campaign/(?P<campaign_id>\d+)/remove/$',
        views.admin_advertising_remove_campaign,
        name='admin_advertising_remove_campaign'
    ),
    url(r'^admin-advertising/ad/(?P<ad_id>\d+)/remove/$',
        views.admin_advertising_remove_ad,
        name='admin_advertising_remove_ad'
    ),
    url(r'^admin-advertising/review/$',
        views.admin_advertising_review,
        name='admin_advertising_review'
    ),
    url(r'^admin-advertising/ad/(?P<ad_id>\d+)/(?P<status>\w+)/$',
        views.admin_advertising_change_status,
        name='admin_advertising_change_status'
    ),

    # Orders
    url(r'^admin-orders/$',
        views.admin_orders,
        name='admin_orders'
    ),    

    # Featured Events
    url(r'^admin-featured/$',
        views.admin_featured,
        name='admin_featured'
    ),
    url(r'^admin-setup-featured/(?P<event_id>\d+)$',
        views.admin_setup_featured,
        name='admin_setup_featured'
    ),
    url(r'^admin-remove-featured/(?P<featured_event_id>\d+)$',
        views.admin_remove_featured,
        name='admin_remove_featured'
    ),
    url(r'^admin-edit-featured/(?P<featured_event_id>\d+)$',
        views.admin_edit_featured,
        name='admin_edit_featured'
    ),
    url(r'^admin-activate-featured/(?P<featured_event_id>\d+)$',
        views.admin_activate_featured,
        name='admin_activate_featured'
    ),
    url(r'^admin-deactivate-featured/(?P<featured_event_id>\d+)$',
        views.admin_deactivate_featured,
        name='admin_deactivate_featured'
    ),
    url(r'^free-try/$',
        views.free_try,
        name='free_try'
    ),
    url(r'^remove-free-try/(?P<account_id>\d+)$',
        views.remove_free_try,
        name='admin_remove_free_try'
    ),
    url(r'^bonus-campaigns/$',
        views.bonus_campaigns,
        name='bonus_campaigns'
    ),
    url(r'^remove-bonus-campaign/(?P<campaign_id>\d+)$',
        views.remove_bonus_campaign,
        name='admin_remove_bonus_campaign'
    ),
    url(r'^change-event-owner-search$',
        views.change_event_owner_search,
        name='change_event_owner_search'
    ),
    url(r'^change-owner/(?P<slug>[^/]+)$',
        views.change_event_owner,
        name='change_event_owner'
    ),

    url(r'^change-owner-ajax/$',
        views.change_event_owner_ajax,
        name='change_event_owner_ajax'
    ),

    url('^change-venue-owner$',
        views.change_venue_owner_search,
        name="change_venue_owner_search"
    ),
    url(r'^change-venue-owner/(?P<venue_account_id>\d+)$',
        views.change_venue_owner,
        name='change_venue_owner'
    ),
    url(r'^mass-event-transfer$',
        views.event_mass_transfer,
        name='mass_event_transfer'),
    url(r'^mass-venue-transfer$',
        views.venue_mass_transfer,
        name='mass_venue_transfer'),
    url(r'^change-venues-owner-ajax/$',
        views.change_venues_owner_ajax,
        name='change_venues_owner_ajax'),

    url(r'^share-stats/(?P<campaign_id>\d+)$',
        views.admin_share_stats,
        name='admin_share_stats'
    ),
    url(r'^unshare-stats/(?P<campaign_id>\d+)/(?P<account_id>\d+)$',
        views.admin_unshare_stats,
        name='admin_unshare_stats'
    ),

    # Venues
    url(r'^admin-venues/$',
        views.admin_venues,
        name='admin_venues'
    ),
    url(r'^admin-edit-venue/(?P<id>\d+)$',
        views.admin_edit_venue,
        name='admin_edit_venue'
    ),
    url(r'^admin-delete-venue/(?P<id>\d+)$',
        views.admin_delete_venue,
        name='admin_delete_venue'
    )
)
