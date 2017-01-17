var Connection = require('./connection')

var keras = new Connection()
var Instructor = new (require('./instructor'))()
var Sketcher = require('./sketcher')
var sketcher = new Sketcher(function(deltas) {
  keras.send('train', {
    points: deltas,
    gesture: Instructor.index
  })
  Instructor.next()
})
