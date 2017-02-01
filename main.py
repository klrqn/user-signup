import webapp2
import validation

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>Month<input type="text" name="month" value={1}></label>
    <br>
    <label>Day<input type="text" name="day" value={2}></label>
    <br>
    <label>Year<input type="text" name="year" value={3}></label>
    <div>{0}</div>
    <br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def writeform(self, error="", month="", day="", year=""):
        self.response.write(form.format(error, month, day, year))

    def get(self):
        self.writeform()

    def post(self):
        # verify the user's input
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = validation.valid_month(user_month)
        day = validation.valid_day(user_day)
        year = validation.valid_year(user_year)

        # on error, render form again
        if not (month and day and year):
            self.writeform("<p style=color:red;> That doesn't look valid to me friend.</p>", user_month, user_day, user_year)
        else:
            self.response.write("Thanks, that data is totally valid!")

        #TODO: include error message

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
