#google_appengine/appcfg.py update google_appengine/helloudacity

import webapp2
import cgi

def escape_html(s):
	s = cgi.escape(s, quote=True)
	return s

form = """
<!DOCTYPE html>

<html>
  <head>
    <title>CS253 Rot13</title>
  </head>
  <body>
	<h4>ROT13, which is short for rotate by 13 places, is a letter
	substitution method by which letters are replaced by a letter
	13 letters before or after it in the alphabet.</h4>
	<h2>Enter some text to Rot13:</h2>
	<form method="post">
	  <textarea name="text"
	  style="height: 100px; width: 400px;">%(flip)s</textarea>
	<br>
	<input type="submit">
	</form>
  </body>
</html>
"""

class Rot13(webapp2.RequestHandler):
	def write_form(self, flip=""):
		self.response.out.write(form % {"flip": escape_html(flip)})

	def get(self):
		self.write_form()

	def post(self):
		flipped = ""
		flip = self.request.get('text')
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		for letter in flip:
			if letter.lower() in alphabet:
				index = alphabet.index(letter.lower())
				if index < 13:
					newLetter = alphabet[index + 13]
				else:
					newLetter = alphabet[index - 13]
				if letter.isupper():
					newLetter = newLetter.upper()
			else:
				newLetter = letter
			flipped += newLetter
			
		self.write_form(flipped)

app = webapp2.WSGIApplication([('/rot13', Rot13)]
								, debug=True)