'use strict';

// Display a text message in the #message box.
function displayMessage(message) {
	$('#message').text(message).fadeIn();
	setTimeout(function() {
		$('#message').fadeOut();
	}, 2000);
}