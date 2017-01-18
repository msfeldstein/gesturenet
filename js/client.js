var Connection = require('./connection')
var keras = new Connection()
var Instructor = new (require('./instructor'))()
var Sketcher = require('./sketcher')

var Plotly = require('plotly.js');

var $ = function(qs) {
  return document.querySelector(qs)
}

var trainingModeBox = $('#training-mode')

var sketcher = new Sketcher(function(deltas) {
  var action = trainingModeBox.checked ? 'train' : 'predict'
  console.log("Sending action", action)
  keras.send(action, {
    points: deltas,
    gesture: Instructor.index
  }) 
  Instructor.next()
}, 300)

keras.addCallback(function(results) {
  plot(results[0])
})

$('#save-weights').addEventListener('click', () => {
  keras.send('save-weights')
})

$('#load-weights').addEventListener('click', () => {
  keras.send('load-weights')
})

function plot(results) {
  Plotly.newPlot($('#chart'), [{
    x: Instructor.instructions,
    y: results,
    type: 'bar'
  }])  
}

console.log(Instructor.instructions)