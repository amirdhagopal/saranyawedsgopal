
from controller import *

import webapp2

app = webapp2.WSGIApplication([(r'/', HomeHandler),
                               (r'/wedding', WeddingHandler)],
                              debug=True)