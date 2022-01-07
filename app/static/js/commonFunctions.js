// Disable Enter Button on all Pages
$(document).keypress(function (event) {
	if (event.which == "13") {
		event.preventDefault();
	}
});
