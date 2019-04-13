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
	retVal = a + b
	return retVal

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
	retVal = a - (b)
	return retVal

def Division(a,b):
	"""
		**Mathematical Division:**
		Divides variables a and b

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

		:return: retVal - value of this operation

		- Special Cases::

			Factorial(0) -- Returns:  1
			Factorial(a); a is not from N + {0} -- Returns None

		- Example::

			Factorial(2)

		- Expected Suceess Response::

			2

	"""

	
	retVal = 1
	if a<1:
        	return None
    	while a!=1:
        	retVal = a * retVal
        	a-=1
    	return retVal	

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

	retVal = a ** b
	return retVal

def Root(a,b):
	"""
		**Mathematical Root:**
		Calculates the value of *b*th root of a

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

		:return: retVal - value of this operaton

		- Special Cases::

			Log(a,b); a or b is <0 -- Returns None

		- Example::

			Log(10,10)

		- Expected Success Result::

			1

	"""
	retVal = log10(a) / log10(b) + 0.00000000000001
	return "{0:.10f}".format(retVal)

def log10(x):
    LN10 = 2.3025850929940456840179914546844
    return ln(x) / LN10;    


def ln(x):
    old_sum = 0.0
    xmlxpl = (x - 1) / (x + 1)
    xmlxpl_2 = xmlxpl * xmlxpl
    denom = 1.0
    frac = xmlxpl
    term = frac
    sum = term

    while sum != old_sum:
    
        old_sum = sum
        denom += 2.0
        frac *= xmlxpl_2
        sum += frac / denom    
    return 2.0 * sum1