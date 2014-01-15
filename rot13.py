import webapp2
import cgi

class Rot13(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Rot13!')

app = webapp2.WSGIApplication([('/rot13', Rot13)]
								, debug=True)