import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<p style="font-size:200%">Hello Launchcode!!</p>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
