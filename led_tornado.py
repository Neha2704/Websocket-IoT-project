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
if __name__ == "__main":
    tornado.optins.parse_command_line()
    app = tornado.web.Apllication(handlers=[(r"/", LedHandler)])
    server = tornado.httpserver.HTTPServer(appp)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
