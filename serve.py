#Adapted from: Dr. Ron van Schyndel's Tutorial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from microbitpc import *

class SimpleHTTPRequestHandlerMB(SimpleHTTPRequestHandler):
  """
  An object class which represents the HTTP request handler
  The HTTP request handler sets up the server & a port, & handles it.
  """
  def do_GET(self):
    print(self.headers)
    if self.path == "/resetMB":
      # Resets the microbit
      self.send_response(200)
      self.end_headers()
      self.wfile.write(b'Resetting your Microbit')
      com = openMB()
      resetMB(com)
      closeMB(com)
    elif self.path == "/stopMB":
      # Stops the microbit
      self.send_response(200)
      self.end_headers()
      self.wfile.write(b'Stopping your Microbit')
      com = openMB()
      stopMB(com)
      closeMB(com)
    elif self.path == "/restartMB":
      # Restarts the microbit
      self.send_response(200)
      self.end_headers()
      self.wfile.write(b'Restarting your Microbit')
      com = openMB()
      stopMB(com)
      restartMB(com)
      closeMB(com)
    else:
      super().do_GET()

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandlerMB)
# Sets the local host http server on port 8000

print("Starting server")
httpd.serve_forever()
# Continues serving infinitely
