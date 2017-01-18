from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json

onGestureCallback = None
clients = []
class MessageHandler(WebSocket):
    def handleMessage(self):
        payload = json.loads(self.data)
        action = payload['action']
        data = payload['data']
        if onGestureCallback != None:
            onGestureCallback(action, data)
        
    def handleConnected(self):
        print self.address, 'connected'
        clients.append(self)

    def handleClose(self):
        print self.address, 'closed'


server = SimpleWebSocketServer('', 8000, MessageHandler)

def onGestureEvent(cb):
    global onGestureCallback
    onGestureCallback = cb

def send(data):
    print("I will send data", data)
    for client in clients:
        print("To client", client)
        client.sendMessage(data)
def start():
    server.serveforever()
    