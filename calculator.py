"""Source code for Calculator by RunySoft

.. moduleauthor:: RunySoft

"""

def Addition(a,b):
	"""
		**Mathematical Addition:**
		Adds viariables a and b.

		:return: retVal - value of this operation

		- Special Cases::

			n/a

		- Example::

			Addition(1,0)

		- Expected Success Response::

			1

	"""
	return lambda retVal : a + b

def Subtraction(a,b):
	"""
		**Mathematical Substraction::**
		Subtracts variables a and b.

		:return: retVal - value of this operation

		- Special Cases::

			n/a

		- Example::

			Subtraction(3,2)

		- Expected Success Response::
			
			1

	"""

	return lambda retVal : a - b

def Division(a,b):
	"""
		**Mathematical Division:**
		Divides variables a and b

		:return: retVal - value of this operation.
		
		- Special Cases::
			
			Division(a,0); a is from (-inf,+inf) -- Returns +infinity
			Division(0,0); -- Returns NaN

		- Example::

			Division(4,2)

		- Expected Success Response::

			2

	"""

	"""
	TODO: code
	"""
def Multiplication(a,b):
	"""
		**Mathematical Muliplication:**
		Multiplies varibles a and b

		:return: retVal - value of this operation

		- Special Cases::

			n/a

		- Example::

			Multiplication(2,2)

		- Expected Success Response::

			4

	"""

	"""
	TODO: code
	"""

def Factorial(a):
	"""
		**Mathematical Factiorial:**
		Calculates the value of *a*!

		:return: retVal - value of this operation

		- Special Cases::

			Factorial(0) -- **Returns:**  1

		- Example::

			Factorial(2)

		- Expected Suceess Response::

			2

	"""

	"""
	TODO: code
	"""

def Exponentiation(a,b):
	"""
		**Mathematical Exponentiation:**
		Calculates the value of *a* to the power of *b*

		:return: retVal - value of this operation

		- Special Cases::

			Exponentiation(a,0); a is from (-inf,+inf) -- Returns 1
		
		- Example::

			Exponentiation(2,1)

		- Expected Success Response::

			2
	"""

	"""
	TODO: code
	"""

def Root(a,b):
	"""
		**Mathematical Root:**
		Calculates the value of *b*th root of a

		:return: retVal - value of this operation

		- Special Cases::

			n/a

		- Example::

			Root(8,3)

		- Expected Success Result::

			2
		
	"""

	"""
	TODO:code
	"""

def Log(a,b):
	"""
		**Mathematical Logarithm:**
		Calculates the value of logarithm of *b* to base *a*

		:return: retVal - value of this operaton

		- Special Cases::

			Log(a,1); a is from (0,+inf) -- Returns 0
			Log(a,b); a is from (-inf,0> or b is from (-inf,0> -- Returns None

		- Example::

			Log(10,10)

		- Expected Success Result::

			1

	"""

	"""
	TODO: code
	"""
