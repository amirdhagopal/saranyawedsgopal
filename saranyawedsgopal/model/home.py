from google.appengine.ext import db
import logging


class Profile(db.Model):
	name = db.StringProperty()
	gender = db.StringProperty(choices=['male','female'])
	phone = db.StringProperty()
	email = db.EmailProperty()
	address = db.TextProperty()
	corporate = db.ReferenceProperty(Corporate, collection_name="profiles")
	city = db.StringProperty()
	pincode = db.StringProperty()
	user_id = db.StringProperty()

	

class ProfileDetail():		
	def save_profile(self, profileContent, profile = Profile()):
		if profile is None:
			profile = Profile()

		for name, property_type in Profile.properties().items():
			logging.info("Setting Field : " + name)
			value = utils.cast(profileContent[name], property_type)			

			setattr(profile, name, value)

		profile.put()
