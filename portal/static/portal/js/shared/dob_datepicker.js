'use strict';

$(document).ready(function () {

	// Date picker for insured date of birth
	$( function() {
		$( "#id_dob" ).datepicker({
			changeMonth: true,
			changeYear: true,
			yearRange: "-100:+0",
			defaultDate: "-25y",
			maxDate: "-16y",
		});
	});

});
