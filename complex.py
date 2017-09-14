class Complex:
	'This is a class for Complex numbers and their operations'
	
	def __init__ (self, real, imag):
		self.r = real
		self.im = imag

	def __repr__(self):
		return '%d + %d j' %(self.r,self.im)
		
	def __add__(self,other):
		sum_real = self.r + other.r
		sum_imag = self.im + other.im
		return '%d + %d j' %(sum_real,sum_imag)
		
	def __sub__(self,other):
		diff_real = self.r - other.r
		diff_imag = self.im - other.im
		return '%d + %d j' %(diff_real,diff_imag)
		
	def __mul__(self,other):
		prod_real = (self.r * other.r) - (self.im*other.im)
		prod_imag = (self.r * other.im) + (self.im*other.r)
		return '%d + %d j' %(prod_real, prod_imag)
		
		
a = Complex(3,4)
b = Complex (2,1)

print (a)
print (b)

print (a+b)
print (a-b)
print (a*b)

print (b-a)
print (b*a)