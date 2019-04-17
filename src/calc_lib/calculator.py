"""Source code for Calculator by RunySoft

.. moduleauthor:: RunySoft

"""

def Addition(a,b):
	"""
		**Mathematical Addition:**
		Adds viariables a and b.
		
		:param a: Addition parameter

		:param b: Addition parameter

		:type a: number 

		:type b: number

		:return: retVal - value of this operation

		- Special Cases::

			n/a

		- Example::

			Addition(1,0)

		- Expected Success Response::

			1

	"""
	retVal = a + b
	return retVal

def Subtraction(a,b):
	"""
		**Mathematical Substraction::**
		Subtracts variables a and b.
		
		:param a: Value to subtract from

		:param b: Subtraction value

		:type a: number 

		:type b: number

		:return: retVal - value of this operation

		- Special Cases::

			n/a

		- Example::

			Subtraction(3,2)

		- Expected Success Response::
			
			1

	"""
	retVal = a - (b)
	return retVal

def Division(a,b):
	"""
		**Mathematical Division:**
		Divides variables a and b
				
		:param a: Value to divide

		:param b: Division value

		:type a: number 

		:type b: number

		:return: retVal - value of this operation.
		
		- Special Cases::
			
			Division(a,0); a is from (-inf,+inf) -- Returns None

		- Example::

			Division(4,2)

		- Expected Success Response::

			2

	"""	
	if b==0:
		return None
	retVal = a / b
	return retVal

def Multiplication(a,b):
	"""
		**Mathematical Muliplication:**
		Multiplies varibles a and b
		
		:param a: Vale to multiply

		:param b: Multiplication value

		:type a: number 

		:type b: number

		:return: retVal - value of this operation

		- Special Cases::

			n/a

		- Example::

			Multiplication(2,2)

		- Expected Success Response::

			4

	"""	
	retVal = a * b
	return retVal	

def Factorial(a):
	"""
		**Mathematical Factiorial:**
		Calculates the value of *a*!
		
		:param a: Value to calculate the factorial of

		:type a: number 

		:return: retVal - value of this operation

		- Special Cases::

			Factorial(0) -- Returns:  1
			Factorial(a); a is not from N + {0} -- Returns None

		- Example::

			Factorial(2)

		- Expected Suceess Response::

			2

	"""

	if a % 1 != 0:
		return None
	retVal = 1
	if a<0:
		return None
	if a==0:
		return 1
	while a!=1:
		retVal = a * retVal
		a-=1
	return retVal	

def Exponentiation(a,b):
	"""
		**Mathematical Exponentiation:**
		Calculates the value of *a* to the power of *b*
		
		:param a: Base of the exponentiation

		:param b: Exponent

		:type a: number 

		:type b: number

		:return: retVal - value of this operation

		- Special Cases::

			Exponentiation(a,0); a is from (-inf,+inf) -- Returns 1
		
		- Example::

			Exponentiation(2,1)

		- Expected Success Response::

			2
	"""

	retVal = a ** b
	return retVal

def Root(a,b):
	"""
		**Mathematical Root:**
		Calculates the value of *b* th root of a
		
		:param a: Base of the root

		:param b: Degree of the root

		:type a: number 

		:type b: number

		:return: retVal - value of this operation

		- Special Cases::

			Root(a); a is <0 -- Return None

		- Example::

			Root(8,3)

		- Expected Success Result::

			2
		
	"""

	if a<0 :
		return None
	retVal = a ** (1/b)
	return retVal

def Log(a,b):
	"""
		**Mathematical Logarithm:**
		Calculates the value of logarithm of *a* to base *b*
		
		:param a: Value to calculate the logarith of

		:param b: Base of the logarithm

		:type a: number 

		:type b: number

		:return: retVal - value of this operaton

		- Special Cases::

			Log(a,b); a or b is <0 -- Returns None

		- Example::

			Log(10,10)

		- Expected Success Result::

			1

	"""

	"""
	TODO: code
	"""
Factorial(8)