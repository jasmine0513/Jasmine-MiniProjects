"""
Jasmine Carrion
jasmine.carrion73@login.cuny.edu
"""
def status_to_message(code):
  status_dict = {
    200: "OK",
    201: "Created",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    418: "I'm a teapot",
    500: "Internal Server Error",
    503: "Service Unavailable",
  }
  return status_dict.get(code, "Unknown")
