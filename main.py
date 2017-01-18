from connect import *
from train import Trainer

def onPrediction(results):
    pass
trainer = new Trainer(onPrediction)
trainer.train(0, 0)
def trainCallback(action, data):
    pass

onTrainEvent(trainCallback)
start()
