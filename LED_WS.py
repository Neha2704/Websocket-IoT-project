import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket

class LedHandler(tornando.websocket.WebSocketHandler):
    def open(self):
        print "Connection opened"
        self.write_message("Connection opened")
        
    def on_close(self):
        print "Connection closed"
        
    def on_message(self, message):
        print "Message received: {}".format(message)
        self.write_message("Message recieved")
