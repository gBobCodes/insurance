/*
Required Functions:
	displayMessage()
	updateUserMenu()	
*/

'use strict';


$(document).ready(function() {

	// Generic code to submit the form via AJAX, instead of normal https.
	// Add the class js-ajaxable-form to the form.
	$('.js-ajaxable-form').submit(function(event) {
		// Prevent default form submission.
		event.preventDefault();

		// Remove the error messages from the form.
		$('form .care-field-error').text('');

		var $form = $(event.target);

		$.ajax({
			type: $form.attr('method'),
			url: $form.attr('action'),
			dataType: 'json',
			data: $form.serialize(),
			encode: true,
			success: function(response, statusText, jqXHR) {
				// Process the response returned by the server ...
				if (response.model === 'User') {
					updateUserMenu(response.instance);
					displayMessage('Account Updated');
				} else if (response.model === 'PasswordChange') {
					displayMessage('Password Changed');
				} else {
					console.log(response.model);
				}
				// Close the modal window.
				$('a.close-modal').click();
			},
			error: function(jqXHR, statusText, errorThrown) {
				console.log("ERROR");
				console.log(jqXHR);
				// Update the error messages on the form.
				$.each( jqXHR.responseJSON, function( fieldID, errorMsg ) {
					$('form #'+fieldID).text(errorMsg);
				});
			},
			complete: function(jqXHR, statusText) {
			},
		});
	});
});


