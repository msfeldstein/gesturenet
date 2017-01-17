const instructions = ['/', '\\', '-', 'o']  

const Instructor = function() {
  this.instructionContainer = document.createElement('h1')
  this.instructionContainer.style.textAlign = 'center'
  document.body.appendChild(this.instructionContainer)
  this.index = 0
  this.next()
}

Instructor.prototype.next = function() {
  this.index = (this.index + 1) % instructions.length
  this.instructionContainer.textContent = "Draw -->   " + instructions[this.index]
}

module.exports = Instructor