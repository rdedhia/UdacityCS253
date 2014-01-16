import webapp2
import re
import cgi

def escape_html(s):
	s = cgi.escape(s, quote=True)
	return s

def user_check(username):
	check = re.compile(r"^[A-Za-z0-9_-]{3,20}$")
	if check.match(username):
		return username

def pass_check(password):
	check = re.compile(r"^.{3,20}$")
	if check.match(password):
		return password

def ver_check(verify, password):
	if verify == password:
		return verify

def mail_check(email):
	if email:
		check = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
		if check.match(email):
			return email
	else:
		return "No email"

form = """
<h2>Signup</h2>
<form method="post">
	<label>
		Username
		<input type="text" name="username" value="%(username)s">
		<span style="color:red">%(u_error)s</span>
	</label>
	<br>
	<label>
		Password
		<input type="password" name="password" value="%(password)s">
		<span style="color:red">%(p_error)s</span>
	</label>
	<br>
	<label>
		Verify Password
		<input type="password" name="verify" value="%(verify)s">
		<span style="color:red">%(v_error)s</span>
	</label>
	<br>
	<label>
		Email (optional)
		<input type="text" name="email" value="%(email)s">
		<span style="color:red">%(error)s</span>
	</label>
	<br><br>
	<input type="submit">
</form>
"""

class SignUp(webapp2.RequestHandler):

	def write_form(self, username="", u_error="",
		password="", p_error="", verify="", v_error="",
		email="", error=""):
		self.response.out.write(form % 
			{"username": escape_html(username), "u_error": u_error,
			"password": escape_html(password), "p_error": p_error,
			"verify": escape_html(verify), "v_error": v_error,
			"email": escape_html(email), "error": error,
			})		

	def get(self):
		self.write_form()

	def post(self):
		u_error = ""
		p_error = ""
		v_error = ""
		error = ""

		username = self.request.get('username')
		password = self.request.get('password')
		verify = self.request.get('verify')
		email = self.request.get('email')
		
		global user
		user = user_check(username)
		pw = pass_check(password)
		ver = ver_check(verify, password)
		mail = mail_check(email)

		if not (user and pw and ver and mail):
			if not user:
				u_error = "Not a valid username"
			if not pw:
				p_error = "Not a valid password"
			else:
				if not ver:
					v_error = "Passwords don't match"
			if not mail:
				error = "Not a valid email"
			self.write_form(username, u_error, "", p_error, 
				"", v_error, email, error)
		else:
			self.redirect('/signup/welcome')

class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Welcome, ' + user + '!')

app = webapp2.WSGIApplication([('/signup', SignUp),
								('/signup/welcome', WelcomeHandler)],
								debug=True)