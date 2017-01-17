from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
class SimpleEcho(WebSocket):
    def handleMessage(self):
        payload = json.loads(self.data)
        action = payload['action']
        data = payload['data']
        print "Received", action, data
        
    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()