$(document).ready(function() {
  $("#newButton").click( function(event) {
    if($('#newForm').hasClass('sneaky')) {
        $('#newForm').removeClass('sneaky');
        $('#joinForm').addClass('sneaky');
    }
});
$("#joinButton").click( function(event) {
    if($('#joinForm').hasClass('sneaky')) {
        $('#joinForm').removeClass('sneaky');
        $('#newForm').addClass('sneaky');
    }
});
});
