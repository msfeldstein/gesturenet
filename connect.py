from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json

onTrainCallback = None

class MessageHandler(WebSocket):
    def handleMessage(self):
        payload = json.loads(self.data)
        action = payload['action']
        data = payload['data']
        print "Received", action
        print onTrainCallback
        if onTrainCallback != None:
            onTrainCallback(action, data)
        
    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'


server = SimpleWebSocketServer('', 8000, MessageHandler)

def onTrainEvent(cb):
    global onTrainCallback
    onTrainCallback = cb
    
def start():
    server.serveforever()
    