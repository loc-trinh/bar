var compliments = ["Excellent choice!", "Greate taste!", "Good choice!", "Fantastic!"];

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){
	$('.button-collapse').sideNav({
      menuWidth: 240, // Default is 240
      closeOnClick: false, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens
    });
    $('.carousel.carousel-slider').carousel({full_width: true});

    $.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
	            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	        }
	    }
	});

	$(".voteup").one("click", function(){
	    Materialize.toast(compliments[getRandomInt(0,4)], 800, 'rounded');
	    $.post("/vote/", 
	    {
	        name: this.getAttribute("name"),
	        type: "upvote"
	    });
	    $(this).hide();
	    $(this).siblings().hide();
	});
	$(".votedown").one("click", function(){
	    Materialize.toast("Not good? Let us know!", 800, 'rounded');
	    $.post("/vote/", 
	    {
	        name: this.getAttribute("name"),
	        type: "downvote"
	    });
	    $(this).hide();
	    $(this).siblings().hide();
	});
});