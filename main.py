from connect import onGestureEvent, send, start
from train import Trainer
import json
def onPrediction(results):
    print("got results", results.tolist())
    msg = json.dumps(results.tolist())
    print("Sending message", msg)
    send(msg)

trainer = Trainer(onPrediction)
def trainCallback(action, data):
    print("Got data from client", data, len(data["points"]))
    trainer.train(data["points"], data["gesture"])

onGestureEvent(trainCallback)
start()
