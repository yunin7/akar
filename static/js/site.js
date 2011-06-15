/**
 * Date: 24.05.11
 * Time: 21:31
 */
function onSmall(id) {
    $("#comment"+id).slideToggle('slow');
}

$(document).ready(function(){
    $("a[rel^='prettyPhoto']").prettyPhoto({
        theme: 'facebook',
        slideshow:5000,
        autoplay_slideshow:true,
        show_title: false
    });
});
