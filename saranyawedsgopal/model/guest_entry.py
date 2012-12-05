from google.appengine.ext import db
import logging

class GuestEntry(db.Model):
	name = db.StringProperty()
	location = db.StringProperty()
	comment = db.StringProperty()
	

class GuestEntryDetail():		
	def save_guest_entry(self, guestEntry= GuestEntry()):
        logging.info("Setting GuestEntry Name: " + guestEntry.name + " Location"+ guestEntry.location)
		guestEntry.put()
