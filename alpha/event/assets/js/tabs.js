$(document).ready(function() {
    $('ul.tabs, table.tabs').each(function() {
        $(this).find('[data-tab-id]').each(function(i) {
            $(this).click(function(){
                var page, tab;
                $(this).addClass('current').siblings().removeClass('current')
                    .closest('div.tabs-container').find('div.box').eq(i).fadeIn(150).siblings('div.box').hide();


                page = $(this).closest(".tabs").data("page-id");
                tab = $(this).data("tab-id");

                $.ajax({
                    url: "/events/save-active-tab/" + page + "/" + tab,
                    dataType: "html",
                    success: function(data) {
                        
                    }
                });
            });
        });
    });
});