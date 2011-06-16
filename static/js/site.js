/**
 * Date: 24.05.11
 * Time: 21:31
 */

var feedback = {};
feedback.init = function(config) {
    if (!(config.button && config.drop && config.popup))
        throw "invalid params";
    config.popup.find('form.feedback').ajaxSubmit({
        'onstart':function(){
            config.popup.addClass('loading');
        },
        'onend':function(){
            config.popup.removeClass('loading');
        },
        'onerror':function(why){
            alert('Error! '+why);
        },
        'onsuccess':feedback.done(config)
    });

    config.button.click(function(){
        config.drop.removeClass('hiding');
        config.popup.removeClass('hiding');
        config.popup.find('input[name=email]').focus();
    });
    config.popup.find('.close').click(feedback.closeit(config));
};

feedback.done = function(config) {
    return function() {
        config.popup.addClass('thanks');
        config.popup.delay(1000).fadeOut(500, feedback.closeit(config));
        config.popup.delay(1000).fadeOut(500);
    };
};

feedback.closeit = function(config) {
    return function(){
        config.drop.addClass('hiding');
        config.popup.addClass('hiding');
        config.popup.removeClass('thanks');
        config.popup.css('display','');
        config.drop.css('display','');
        config.popup.find('textarea').val('');
        config.popup.find('input[name=subject]').val('');
    };
};

$(function(){
    feedback.init({
        'button':$('#feedback_button'),
        'drop':$('#feedback_drop'),
        'popup':$('#feedback_popup')
    });
});

$(document).ready(function(){
    $("a[rel^='prettyPhoto']").prettyPhoto({
        theme: 'facebook',
        slideshow:5000,
        autoplay_slideshow:true,
        show_title: false
    });
    $(".content .images img.icon").click(function(){
        $(".content .images .thumbnail").hide();
        $(".content .property-description").hide();
        $("#" + this.getAttribute("id").replace('icon', 'thumbnail')).fadeIn();
        $("#" + this.getAttribute("id").replace('icon', 'description')).fadeIn();
    });
});
