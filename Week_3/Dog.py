class Dog():

	#Constructer function
	def __init__(self, color, weight, eyeColor, name):
		self.furColor = color
		self.weight = weight
		self.eyeColor = eyeColor
		self.name = name

	#Methods
	def bark(self):
		print("Woof")

	def wag(self):
		print("Wagging Tail")

	def run(self):
		print("Your dog is running away")

Toto = Dog("Brown", 25, "Blue", "Name")

Toto.run()
