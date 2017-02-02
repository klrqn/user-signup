import webapp2
import valid

form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Sign Up</title>
    </head>
<body>
    <h2>Sign Up</h2>
    <form method="post">
        <label>Username<input type="text" name="username" value={0}></label>{4}
        <br>
        <label>Password<input type="password" name="password" value={1}></label>{5}
        <br>
        <label>Password Check<input type="password" name="verify" value={2}></label>
        <br>
        <label>Email (optional)<input type="text" name="email" value={3}></label>{6}
        <br>
        <input type="submit" value="sign up dude!">
    </form>
</body>
    """


class MainHandler(webapp2.RequestHandler):

    def writeform(self, username="", password="", verify="", email="", error="", error_pw="", error_email=""):
         self.response.write(form.format(valid.escaped_html(username),
                                         valid.escaped_html(password),
                                         valid.escaped_html(verify),
                                         valid.escaped_html(email),
                                         error,
                                         error_pw,
                                         error_email))

    def get(self):
        self.writeform()

    def post(self):

        # have_error = False
        errorDict = {"username":"<b style=color:red;> Not a valid username </b>",
                     "password":"<b style=color:red;> Not a valid password </b>",
                     "pw_match":"<b style=color:red;> Passwords don't match </b>",
                     "email":"<b style=color:red;> Not a valid email </b>"}

        # get the users input for the 4 fields
        username = self.request.get("username")
        password = self.request.get("password")
        password_check = self.request.get("verify")
        email = self.request.get("email")

        # verify the inputs
        valid_username = valid.verify_username(username)
        valid_password = valid.verify_password(password)
        valid_email = valid.verify_email(email)

        if not valid_username:
            self.writeform(username, "", "", email, errorDict["username"])

        elif not valid_password:
            self.writeform(username, "", "", email, "", errorDict["password"])

        elif password != password_check:
            self.writeform(username, "", "", email, "", errorDict["pw_match"])

        elif not valid_email:
            self.writeform(username, "", "", email, "", "", errorDict["email"])

        if valid_username and valid_password and valid_email:
            self.redirect('/welcome?username=' + username)


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        content = "Welcome " + username
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
