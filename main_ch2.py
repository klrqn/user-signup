import webapp2
import valid
import cgi

form="""
<h2>Login</h2>
<form method="post">
    <br>
    <label>Username<input type="text" name="username" value={0}></label>{1}
    <br>
    <label>Password<input type="password" name="password" value={2}></label>{3}
    <br>
    <label>Password Check<input type="password" name="password_check" value={4}></label>{5}
    <br>
    <label>Email (optional)<input type="text" name="email" value={6}></label>{7}
    <input type="submit">
</form>
"""

def escape_html(s):
    return cgi.escape(s, quote=True)

class MainHandler(webapp2.RequestHandler):
    def writeform(self, error="", month="", day="", year=""):
        self.response.write(form.format(error,
                                        escape_html(month),
                                        escape_html(day),
                                        escape_html(year)))

    def get(self):
        self.writeform()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        # verify the user's input
        month = valid.valid_month(user_month)
        day = valid.valid_day(user_day)
        year = valid.valid_year(user_year)

        # on error, render form again
        if not (month and day and year):
            self.writeform("<p style=color:red;> That doesn't look valid to me friend.</p>", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks, that data is totally valid!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler)
], debug=True)
