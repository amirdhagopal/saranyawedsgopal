
from controller import *

import webapp2

app = webapp2.WSGIApplication([(r'/', HomeHandler)],
                              debug=True)