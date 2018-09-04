(function ($) {

    /*---------------------
      Venobox
    --------------------- */
    var veno_box = $('.venobox');
    veno_box.venobox({
        arrowsColor: 'rgba(40,80,160,0.7)',
        spinner: 'three-bounce',
        closeColor: 'red',
        closeBackground: 'rgba(0,0,0,0.5)'
    });


    $("#certificates-row").slick({
        infinite: false,
        dots: true,
        appendDots: $("#slide-dots-anchor")
      });

    if ($('.single-certificate').length <= 1)
        $('.slick-dots').css('visibility', 'hidden');
})(jQuery);