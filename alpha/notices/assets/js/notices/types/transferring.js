;(function($, window, document, undefined) {
    'use strict';

    $(document).ready(function() {
        var links = "[data-type=transferring_accept_link], [data-type=transferring_reject_link]";
        $("body").on("click", links, function() {
            var link = $(this);
            var csrf = link.closest(window.noticesService.noticeItemSelector)
                           .find("input[name=csrfmiddlewaretoken]").val();
            var noticeId = link.data("notice-id");
            var noticeItem = link.closest(window.noticesService.noticeItemSelector);

            $.post(link.attr("href"), {"csrfmiddlewaretoken": csrf, "notice_id": noticeId}, function(data) {
                if(data.success) {
                    noticeItem.remove();
                }
            }, 'json');

            return false;
        });

        $("[data-type=accordion]").each(function() {
            $(this).accordion({
                collapsible: true,
                active: false
            });
        });
    });
})(jQuery, window, document);