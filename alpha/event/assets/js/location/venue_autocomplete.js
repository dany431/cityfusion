;(function($, window, document, undefined) {
    'use strict';
    var google = window.google;

    function VenueAutocomplete(){
        var that = this,
            location_name_input = $('#id_city_0'),
            location_point_input = $('#id_city_1'),
            map_container = $('.location_map');

        this.initSuggestForm();
        this.initGeocomplete(location_name_input, location_point_input, map_container);

        $("#id_place").on("blur", function() {
            $(".pac-container").removeClass("show");
        });

        $("#id_place").on("focus", function() {
            $(".pac-container").addClass("show");
        });
    }

    VenueAutocomplete.prototype = {
        initSuggestForm: function(){
            this.suggestForm = new window.SuggestForm();
        },
        initGeocomplete: function(location_name_input, location_point_input, map_container){
            var latlng,
                that = this;
            $(location_name_input).on("autocompleteselect", function(event, ui){
                if ($(location_point_input).val()) {
                    var point = $(location_point_input).val().split(','), identifier;

                    $(this).parent().find("[name=city_identifier]").val(point[0]);
                    
                    latlng = new google.maps.LatLng(parseFloat(point[2]), parseFloat(point[1]));

                    that.suggestForm.suggestMap.setLocationFromMap(latlng);
                } else {
                    var lng = $("#id_location_lng").val(),
                        lat = $("#id_location_lat").val();

                    latlng = new google.maps.LatLng(parseFloat(lat), parseFloat(lng));
                    that.suggestForm.suggestMap.setLocationFromMap(latlng);
                    $("#id_linking_venue_mode").val("GOOGLE");
                }

            });

            if(!$("#id_place").data("autocomplete-binded")) {
                $("#id_place").geocomplete({
                    details: ".geo-details",
                    detailsAttribute: "data-geo",
                    types: ['geocode', 'establishment'],
                    componentRestrictions: {
                        country: 'ca'
                    }
                }).bind("geocode:result", function(event, result) {
                    $("#id_venue_name").val("");
                    $("#id_street").val("");
                    $("#id_city_0").val("");
                    if($("#id_tags__tagautosuggest").length !== 0) {
                        $("#id_tags__tagautosuggest")[0].tagspopup.loadTagsForCityByCityName();
                    }

                    Cityfusion.userLocationLat = result.geometry.location.lat();
                    Cityfusion.userLocationLng = result.geometry.location.lng();

                    that.suggestForm.suggestMap.setLocation(Cityfusion.userLocationLat, Cityfusion.userLocationLng);

                    window.setTimeout(that.setVenueText.bind(that), 1);
                    $("#id_linking_venue_mode").val("GOOGLE");
                });
            }
        },
        setVenueText: function(){
            var address = $("#id_geo_address").val(),
                venue = $("#id_geo_venue").val();
            if(address.indexOf(venue)===-1){
                $("#id_place").val(
                    $("#id_geo_venue").val()+", "+$("#id_geo_address").val()
                );
            }
        }
    };

    window.VenueAutocomplete = VenueAutocomplete;

})(jQuery, window, document);