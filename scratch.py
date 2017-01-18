from train import Trainer

def onPrediction(results):
    pass

trainer = Trainer(onPrediction)
for i in range(10):
    points = [
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0]
    ]
    trainer.train([
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0]
    ], 0)
    trainer.train([
        [1,0],
        [1,0],
        [2,0],
        [3,0],
        [4,0],
        [6,0],
        [7,0]
    ], 1)
    trainer.train([
        [1,0],
        [2,0],
        [3,0],
        [4,0],
        [5,0],
        [7,0],
        [8,0],
        [9,0]
    ], 1)
    trainer.train([
        [0,1],
        [0,2],
        [0,3],
        [0,4],
        [0,5],
        [0,6],
        [0,7],
        [0,7]
    ], 3)