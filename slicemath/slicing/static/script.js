$(document).ready(function(){
$("#submit").click(function(event){
    $("#p").replaceWith($("#p1").text());
    return false;
});
});
