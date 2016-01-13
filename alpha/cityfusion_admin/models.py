from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from utils import run_async
from django.contrib.sites.models import Site

current_site = Site.objects.get_current().domain

class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(processed=False)


class ReportEvent(models.Model):
    event = models.ForeignKey("event.Event")
    account = models.ForeignKey("accounts.Account", blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    processed  = models.BooleanField(default=False)

    active = ActiveManager()

    def process(self):
        self.processed = True
        self.save()


class ClaimEvent(models.Model):
    event = models.ForeignKey("event.Event")
    account = models.ForeignKey("accounts.Account")
    message = models.TextField(blank=True, null=True)
    processed  = models.BooleanField(default=False)

    active = ActiveManager()

    def process(self):
        self.processed = True
        self.save()


@run_async
def send_report_to_managers(sender, instance, created, **kwargs):
    if created:        
        html_message = render_to_string('cf-admin/email/report_email.html', {
            'report': instance,
            'site': current_site            
        })

        mail_managers("Cityfusion. Report was created", html_message, html_message=html_message)


@run_async
def send_claims_to_managers(sender, instance, created, **kwargs):
    if created:
        html_message = render_to_string('cf-admin/email/claim_email.html', {
            'claim': instance,
            'site': current_site
        })

        mail_managers("Cityfusion. Claim was created", html_message, html_message=html_message)

post_save.connect(send_report_to_managers, sender=ReportEvent)
post_save.connect(send_claims_to_managers, sender=ClaimEvent)


CF_ADMIN_MENU = {
    "cfadmin_home": {
        "urlname": "cfadmin_home",
        "linktext": "Home"
    },
    "transfer_to_owner": {
        "urlname": "change_event_owner_search",
        "linktext": "Transfer"
    },
    "report_event": {
        "urlname": "report_event_list",
        "linktext": "Reports"
    },
    "claim_event": {
        "urlname": "claim_event_list",
        "linktext": "Claims"
    },
    "admin_advertising": {
        "urlname": "admin_advertising",
        "linktext": "Ads"
    },
    "admin_featured": {
        "urlname": "admin_featured",
        "linktext": "Featured Event"
    },
    "free_try": {
        "urlname": "free_try",
        "linktext": "Free try"
    },
    "import_facebook_events": {
        "urlname": "import_facebook_events",
        "linktext": "Import from Facebook"
    },
    "bonus_campaigns": {
        "urlname": "bonus_campaigns",
        "linktext": "Bonus campaigns"
    },
    "orders": {
        "urlname": "admin_orders",
        "linktext": "Orders"
    },
    "venues": {
        "urlname": "admin_venues",
        "linktext": "Venues"
    }
}