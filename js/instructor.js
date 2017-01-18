const instructions = ['/', '\\', '-', 'o', 'L']  

const Instructor = function() {
  this.instructionContainer = document.createElement('h1')
  this.instructionContainer.className = 'instructor'
  document.body.appendChild(this.instructionContainer)
  this.index = 0
  this.next()
  this.instructions = instructions
}

Instructor.prototype.next = function() {
  this.index = (this.index + 1) % instructions.length
  this.instructionContainer.textContent = `Draw -->   ${instructions[this.index]} (${this.index})`
}

Instructor.instructions = instructions

module.exports = Instructor