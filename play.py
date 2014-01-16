# file for playing with regular expressions

import re

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

# if not username: return username error
# if not password: return password error
# if password and not verify: return verify error
# if not email: return email error; if "No email": return None

# Errors must be triggered for everything that's wrong
# Email is only optional, but has to be valid
# Verify is only relevant if the password is suitable
# The username must pass into the next class, is using a global smart?

# Send GET -> get form from server
# Send POST -> send data to the server with form
# Validation occurs on the server
# If correct, request new page and POST username? not sure
# If incorrect, get form from server again and POST errors