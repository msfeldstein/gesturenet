from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json

clientCallback = None
clients = []
class MessageHandler(WebSocket):
    def handleMessage(self):
        payload = json.loads(self.data)
        action = payload['action']
        data = payload['data']
        if clientCallback != None:
            clientCallback(action, data)
        
    def handleConnected(self):
        print self.address, 'connected'
        clients.append(self)

    def handleClose(self):
        print self.address, 'closed'


server = SimpleWebSocketServer('', 8000, MessageHandler)

def onClientMessage(cb):
    global clientCallback
    clientCallback = cb

def send(data):
    for client in clients:
        client.sendMessage(data)
def start():
    server.serveforever()
    