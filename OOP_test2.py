class fraction:
	'This is a class for a type of data called Fraction'
	
	def __init__(self,num,den):
			self.num = num	
			self.den = den
			
	def __repr__(self):
		return str(self.num) + '/' + str(self.den)
		
	def __add__(self,other):
		sum_num = (self.num*other.den) + (self.den*other.num)
		sum_den = (self.den*other.den)
		return sum_num/sum_den
		
	def __sub__(self,other):
		diff_num = (self.num*other.den) - (self.den*other.num)
		diff_den = (self.den*other.den)
		return diff_num/diff_den
		
	def mul (self,other):
		prod_num = self.num*other.num
		prod_den = self.den*other.den
		return prod_num/prod_den
		
	def  div(self,other):
		div_num = self.num*other.den
		div_den = self.den*other.num
		return div_num/div_den
		
	def inv(self):
		return self.den/self.num
		
a = fraction(3,4)
b = fraction(5,6)

print (a)
print (b)

print (a+b)

print (a-b)

print (fraction.mul(a,b))

print (fraction.div(a,b))

print (fraction.div(b,a))

fraction.inv(a)
fraction.inv(b)