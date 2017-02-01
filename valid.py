import cgi
import re

def escaped_html(s):
    return cgi.escape(s, quote=True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(s):
    return USER_RE.match(s)

PW_RE = re.compile("^.{3,20}")
def valid_password(s):
    return PW_RE.match(s)

EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
def valid_email(s):
    return EMAIL_RE.match(s)