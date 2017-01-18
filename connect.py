from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json

onGestureCallback = None

class MessageHandler(WebSocket):
    def handleMessage(self):
        payload = json.loads(self.data)
        action = payload['action']
        data = payload['data']
        print "Received", action
        print onGestureCallback
        if onGestureCallback != None:
            onGestureCallback(action, data)
        
    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'


server = SimpleWebSocketServer('', 8000, MessageHandler)

def onGestureEvent(cb):
    global onGestureCallback
    onGestureCallback = cb

def send(data):
    pass
def start():
    server.serveforever()
    