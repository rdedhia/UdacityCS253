import webapp2
import cgi

def escape_html(s):
	s = cgi.escape(s, quote=True)
	return s

form = """

<h4>ROT13, which is short for rotate by 13 places, is a letter
substitution method by which letters are replaced by a letter
13 letters before or after it in the alphabet.</h4>
<h2>Enter some text to Rot13:</h2>

<form method="post">
	<textarea name="text" style="height: 100px; 
		width: 400px;">Hello!</textarea>
	<br>
	<input type="submit">
</form>
"""

class Rot13(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(form)

	def post(self):
		

app = webapp2.WSGIApplication([('/rot13', Rot13)]
								, debug=True)