class Dog:
	def __init__(self,breed,color):		# "self" is the brain of the object
		self.breed=breed
		self.color=color
		
	def speak(self):
		print("bhou...bhou")
	def jump(self):
		print("I am jumping")
		
	def __del__(self):
		print("Good Bye!")
	
tommy=Dog("german shepherd","brown")
tommy.speak()
tommy.jump()
print(tommy.breed)
print(tommy.color)

