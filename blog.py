# Front page at /blog
# Form to create new entries at /blog/newpage
# Form method of POST, not GET
# Form input boxes with names 'subject' and 'content'
# New page for each entry? I'm not sure

# Use jinja with HTML templating to use multiple files
# Use another Handler for rendering

import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = 
	jinja2.FileSystemLoader(template_dir), autoescape = True)

class Blog(webapp2.RequestHandler):
	def render(self, template, **params):
		page = jinja_env.get_template(template)
		self.response.out.write(page.render(params))

	def render_home(self, subject="", content="", error=""):
		self.render("blog.html", subject=subject, content=content, 
			error=error)

	def get(self):
		self.render_home()

	def post(self):
		subject = self.request.get('subject')
		content = self.request.get('content')

		if subject and content:
			self.response.out.write('thanks!')
		else:
			error = "Please enter both a subject and some content"
			self.render_home(subject, content, error)

class Submission(db.Model):
	

class NewPage(webapp2.RequestHandler):
	pass

app = webapp2.WSGIApplication([('/blog', Blog),
								('/blog/newpage', NewPage)]
								, debug=True)

