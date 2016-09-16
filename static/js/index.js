jQuery(document).ready(function ($) {

	var slideCount = $('#slider ul li').length;
	var slideWidth = $('#slider ul li').width();
	var slideHeight = $('#slider ul li').height();
	var sliderUlWidth = slideCount * slideWidth +80 ; // (10*4)*2 where 10 is margin between li elements.

	$('#slider').css({ width: sliderUlWidth, height: slideHeight });

	$('#slider ul').css({ width: sliderUlWidth /*, marginLeft: - slideWidth */ });

    $('#slider ul li:last-child').prependTo('#slider ul');

    function moveLeft() {
        $('#slider ul').animate({
            left: + slideWidth
        }, 200, function () {
            $('#slider ul li:last-child').prependTo('#slider ul');
            $('#slider ul').css('left', '');
        });
    };

    function moveRight() {
        $('#slider ul').animate({
            left: - slideWidth
        }, 200, function () {
            $('#slider ul li:first-child').appendTo('#slider ul');
            $('#slider ul').css('left', '');
        });
    };

    $('a.control_prev').click(function () {
        moveLeft();
    });

    $('a.control_next').click(function () {
        moveRight();
    });

  $("#slider ul li").on("swipeleft",function(){
    //alert("You swiped left!");
    moveRight();
  });

  $("#slider ul li").on("swiperight",function(){
    //alert("You swiped left!");
    moveLeft();
  });

});
