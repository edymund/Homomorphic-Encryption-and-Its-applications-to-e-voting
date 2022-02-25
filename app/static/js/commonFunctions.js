// Disable Enter Button on all Pages
// $(document).keypress(function (event) {
// 	if (event.which == "13") {
// 		event.preventDefault();
// 	}
// });
$(document).ready(function() {

    $(window).keydown(function(event){

        if((event.keyCode == 13) && ($(event.target)[0]!=$("textarea")[0]&& ($(event.target)[0]!=$("textarea")[1]))) 
    {

            event.preventDefault();

            return false;

        }

    });

});