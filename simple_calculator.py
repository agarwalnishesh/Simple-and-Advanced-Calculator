from stack import Stack

class SimpleCalculator:
	def __init__(self):
		"""
		Instantiate any data attributes
		"""
		self.history = []
		pass

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		self.expression = input_expression
		s=''
		c=0
		L = self.expression.split()
		for i in L:
			s=s+i
		for j in '+-/*':
			for i in s:
				if j==i:
					c+=1
		if c!=1:
			k = (self.expression,"Error")
			self.history.append(k)
			return 'Error'
		if '+' in s:
			L=s.split('+')
			L=list(filter(None,L))
			if len(L)==2:
				k = (self.expression,float(L[0]) + float(L[1]))
				self.history.append(k)
				return float(L[0]) + float(L[1])
			else:
				k = (self.expression,"Error")
				self.history.append(k)
				return 'Error'
		elif '/' in s:
			L=s.split('/')
			L=list(filter(None,L))
			if len(L)==2:
				k = (self.expression,float(L[0]) / float(L[1]))
				self.history.append(k)
				return float(L[0]) / float(L[1])
			else:
				k = (self.expression,"Error")
				self.history.append(k)
				return 'Error'
		elif '*' in s:
			L=s.split('*')
			L=list(filter(None,L))
			if len(L)==2:
				k = (self.expression,float(L[0]) * float(L[1]))
				self.history.append(k)
				return float(L[0]) * float(L[1])
			else:
				k = (self.expression,"Error")
				self.history.append(k)
				return 'Error'
		elif '-' in s:
			L=s.split('-')
			L=list(filter(None,L))
			if len(L)==2:
				k = (self.expression,float(L[0]) - float(L[1]))
				self.history.append(k)
				return float(L[0]) - float(L[1])
			else:
				k = (self.expression,"Error")
				self.history.append(k)
				return 'Error'
		pass

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		self.history = self.history[::-1]
		return self.history

		pass
