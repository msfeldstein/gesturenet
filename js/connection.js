const Connection = function(port) {
  port = port || 8000
  var url = `ws://localhost:${port}/`
  console.log("Connecting to ", url)
  var connection = new WebSocket( url )
  console.log(connection)
  // When the connection is open, send some data to the server
  connection.onopen = function (action, data) {
    console.log('Connected')
  }

  // Log errors
  connection.onerror = function (error) {
    console.log('WebSocket Error ' + error);
  }; 
  
  this.connection = connection
}

Connection.prototype.addCallback = function(cb) {
  this.connection.onmessage = cb; 
}

Connection.prototype.send = function(action, data) {
  var json = JSON.stringify({
    action,
    data
  })
  console.log("sending ", json)
  this.connection.send(json);
}

module.exports = Connection