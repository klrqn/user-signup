import cgi
import re

def escaped_html(s):
    return cgi.escape(s, quote=True)

# match = re.search(pattern, string)
# if match:
#    process(match)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def verify_username(s):
    return s and USER_RE.match(s)

PW_RE = re.compile("^.{3,20}")
def verify_password(s):
    return s and PW_RE.match(s)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def verify_email(email):
    return not email or EMAIL_RE.match(email)