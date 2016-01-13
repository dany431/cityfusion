;(function($, window, document, undefined) {
    'use strict';

    var EventPage = function(){
        this.initEventActions();
        $(".event-details-primary-content a#photoFancy").fancybox({
            'hideOnContentClick': true
        });

        var rightHeight = $(".secondary-content").outerHeight() + $(".rotation-right-container").outerHeight();
        var leftHeight = $(".event-details__title").outerHeight() + $(".event-wrapper").outerHeight();
        $.each(["attachments", "tags"], function(i, selector) {
            if($("." + selector).length !== 0) {
                leftHeight += $("." + selector).outerHeight();
            }
        });

        leftHeight -= $(".description").outerHeight();

        var scrollHeight = rightHeight - leftHeight - 15; // "15px" value chosen empirically
        if(scrollHeight > 0) {
            $("[data-type=event_description]").each(function(i, obj) {
                $(obj).slimScroll({
                    height: scrollHeight + "px",
                    alwaysVisible: true
                });
            });
        }

        $(".venue_map_preview").on("click", this.showMap.bind(this));

        this.reportEvent = new ReportEvent();
        this.claimEvent = new ClaimEvent();
        this.daysSwitcher = new EventDaysSwitcher();
        this.imageViewer = new ImageViewer();
        this.similarEvents = new SimilarEvents();
    };

    EventPage.prototype = {
        initEventActions: function(){
            this.eventActions = new window.EventActions($(".event-details-block"));
        },
        showMap: function(){
            var point = new google.maps.LatLng(window.venue_latitude, window.venue_longtitude),
                options = {
                    zoom: 14,
                    center: point,
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                },
                venue_account_map = new google.maps.Map(document.getElementById("venue_map"), options),
                marker = new google.maps.Marker({
                    map: venue_account_map,
                    position: point,
                    draggable: false
                });

            $.fancybox(document.getElementById("venue_map"), {
                autoSize: true,
                closeBtn: true,
                hideOnOverlayClick: false
            });

            google.maps.event.trigger(venue_account_map, 'resize');
            venue_account_map.panTo(point);       
        }
    };    

    $(document).on("ready page:load", function(){
        window.eventPage = new EventPage();
    });

})(jQuery, window, document);