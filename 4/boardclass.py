class Board:

	def __init__(self,row0,row1,row2,row3,row4,name):
		self.row0 = row0.split()
		self.row1 = row1.split()
		self.row2 = row2.split()
		self.row3 = row3.split()
		self.row4 = row4.split()
		self.name = str(name)
		self.whole = [self.row0,self.row1,self.row2,self.row3,self.row4]
		self.bingoed = False

	def __str__(self):
		#return 'this board has ' + '\n' + str(self.row0) + '\n' + str(self.row1) + '\n' + str(self.row2) + '\n' + str(self.row3) + '\n' + str(self.row4)
		return f"{self.name}: '\n' {self.whole[0]} '\n' {self.whole[1]} '\n' {self.whole[2]} '\n' {self.whole[3]} '\n' {self.whole[4]}"

	def mark(self,number):
		number = str(number)
		if number in self.whole[0]:
			print(f"{number} is in row 0 of {self.name}")
			for a in range(0, len(self.row0)):
				if self.row0[a] == number:
					self.row0[a] += "a"
	
		if number in self.whole[1]:
			print(f"{number} is in row 1 of {self.name}")
			for a in range(0, len(self.row1)):
				if self.row1[a] == number:
					self.row1[a] += "a"
		
		if number in self.whole[2]:
			print(f"{number} is in row 2 of {self.name}")
			for a in range(0, len(self.row2)):
				if self.row2[a] == number:
					self.row2[a] += "a"
		
		if number in self.whole[3]:
			print(f"{number} is in row 3 of {self.name}")
			for a in range(0, len(self.row3)):
				if self.row3[a] == number:
					self.row3[a] += "a"
		
		if number in self.whole[4]:
			print(f"{number} is in row 4 of {self.name}")
			for a in range(0, len(self.row4)):
				if self.row4[a] == number:
					self.row4[a] += "a"