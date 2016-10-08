class FormCache():
	"""
	A place to temporarily hold form values entered by the user.
	Class variables will be dynamically added to this class.
	Those values will disappear when the web server is restarted,
	but that is ok because they are just Searches and Filters
	which the user can enter again.

	An improvement could be using JSON fields in DB model, and saving
	them in the DB.
	"""

	@classmethod
	def get_form_cache(cls, cache_name):
		"""Return the previously saved form values from the cache. """
		try:
			return getattr(cls, cache_name)
		except AttributeError:
			return None
	
	@classmethod
	def set_form_cache(cls, cache_name, values):
		"""Save the user entered values in the cache. """
		setattr(cls, cache_name, values)
