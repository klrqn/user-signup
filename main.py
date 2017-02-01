import webapp2
import valid

form = """
<style type="text/css">
      .label {text-align: right}
      .error {color: red}
</style>
<h2>Login</h2>
<form method="post">
    <label>Username<input type="text" name="username" value={0}></label>{1}
    <br>
    <label>Password<input type="password" name="password" value={2}></label>{3}
    <br>
    <label>Password Check<input type="password" name="verify" value={4}></label>{5}
    <br>
    <label>Email (optional)<input type="text" name="email" value={6}></label>{7}
    <input type="submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):

    def writeform(self, username="", usernameError="", password="", passwordError="", verify="", verifyError="", email="", emailError=""):
         self.response.write(form)


    def get(self):
        return self.writeform()

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        password_check = self.request.get("verify")
        email = self.request.get("email")

        valid_username = valid.valid_username(username)
        valid_password = valid.valid_username(password)
        valid_verify = valid.valid_username(password_check)
        valid_email = valid.valid_username(email)

        if not (valid_username and valid_password and valid_verify and valid_email):
            self.writeform(username, "ERROR", password, password_check, email)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)