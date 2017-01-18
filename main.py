from connect import onGestureEvent, send, start
from train import Trainer

def onPrediction(results):
    pass
trainer = Trainer(onPrediction)
def trainCallback(action, data):
    print("Got Data", data, len(data["points"]))
    pass

onGestureEvent(trainCallback)
start()
