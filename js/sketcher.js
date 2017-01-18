var Touch = require('touches')

const Sketcher = function(listener, size) {
  var deltas = []
  size = size || 512
  
  var canvas = document.createElement('canvas')
  canvas.width = size
  canvas.height = size
  canvas.style.backgroundColor = 'black'
  document.body.appendChild(canvas)
  var ctx = canvas.getContext('2d')
  
  var mouseDown = false
  Touch(canvas)
    .on('start', function(e) {
      mouseDown = true
      this.lastEvent = e
      ctx.strokeStyle = 'white'
      ctx.moveTo(e.layerX, e.layerY)
    })
    .on('move', function(e) {
      if (!mouseDown) return
      ctx.lineTo(e.layerX, e.layerY)
      ctx.stroke()
      deltas.push([
        e.layerX - this.lastEvent.layerX,
        e.layerY - this.lastEvent.layerY
      ])
      this.lastEvent = e
    })
    .on('end', function() {
      mouseDown = false
      listener(deltas)
      deltas = []
      canvas.width = canvas.width
    })
}

module.exports = Sketcher