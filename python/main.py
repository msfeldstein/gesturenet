from connect import onClientMessage, send, start
from train import Trainer
import json
def onPrediction(results):
    print("got results", results.tolist())
    msg = json.dumps(results.tolist())
    print("Sending message", msg)
    send(msg)

trainer = Trainer(onPrediction)
def clientListener(action, data):
    print("Got data from client",action)
    if action == 'train':
        trainer.train(data["points"], data["gesture"])
    if action == 'predict':
        trainer.predict(data["points"])
    if action == 'load-weights':
        trainer.load()
    if action == 'save-weights':
        print("I should save the weights")
        trainer.save()

onClientMessage(clientListener)
start()
