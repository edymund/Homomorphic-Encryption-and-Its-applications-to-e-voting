// Adds a timer to show and hide messages when page loads
$(document).ready(function() {
	showMessages();
	setTimeout(removeMessages, 3000);
});

// Show all messages
function showMessages(){
	$("#errorMsg").slideDown();
	$("#msg").slideDown();
}

// Hide all messages
function removeMessages() {
	$("#errorMsg").slideUp();
	$("#msg").slideUp();
}