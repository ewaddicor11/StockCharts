import os
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
    	self.send_response(200)
    	self.send_header('content-type', 'text/html')
    	self.end_headers()

    	if self.path == '/':
    		self.path = 'app.html'
    		
    	query_components = parse_qs(urlparse(self.path).query)
    	if 'tickerSymbol' in query_components:
    		tickerSymbol = query_components["tickerSymbol"][0]
    	else:
    		tickerSymbol = ''

    	if tickerSymbol != '':
    		shellCommand = 'python StockApp.py ' + tickerSymbol
    		stream = os.popen(shellCommand)
    		output = stream.read()
    		output

    	return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
    	self.send_response(200)
    	self.send_header('content-type', 'text/html')
    	self.end_headers()

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
my_server.serve_forever()

#from http.server import *
#import socketserver

#class MyHttpRequestHandler(SimpleHTTPRequestHandler):
#    def do_GET(self):
#        if self.path == '/':
#            self.path = 'mywebpage.html'
#        return SimpleHTTPRequestHandler.do_GET(self)


#def main():
#	PORT = 8000
#	server_address = ('localhost', PORT)
#	server = HTTPServer(server_address, echoHandler)
#	print('Server running on port %s' % PORT)
#	server.serve_forever()

#if __name__ == '__main__':
#	main()