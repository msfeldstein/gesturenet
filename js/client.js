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
}, 300)

keras.addCallback(function(e) {
  console.log("Message from server ", arguments)
  console.log(e.data)
  debugger
})
