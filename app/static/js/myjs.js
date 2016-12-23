$(document).ready(function(){
	$('.button-collapse').sideNav({
      menuWidth: 240, // Default is 240
      closeOnClick: false, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens
    });
     $('.carousel.carousel-slider').carousel({full_width: true});

});

var resizeTimer;
$(window).resize(function() {
	clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function resizeRank(){
		if ($(window).width() < 600){
			$('.first').insertBefore($('.second'));
		}else{
			$('.second').insertBefore($('.first'));
		}
	}, 100);
});