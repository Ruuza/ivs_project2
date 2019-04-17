#!/usr/bin/env python3
import unittest
import sys
sys.path.append('../calc_lib')
import calculator as calc

class TestCalculator(unittest.TestCase):
	def test_addition(self):
		"""
		Tests the correct functionality of the Addition function
		"""
		a = [1,1,-2,1,3,0.5,1.5,0.5,1E42,1,1]
		b = [1,0,-2,-2,-2,0.5,0.25,-0.75,1E42,1E-1,-1E-1]
		expectedResult = [2,1,-4,-1,1,1.0,1.75,-0.25,2E42,1.1,9E-1]
		print("......Addition Tests......")
		for i in range(0,len(a)):
			result = calc.Addition(a[i],b[i])
			if not self.assertEqual(expectedResult[i],result):
				print("--TEST-- Addition(%6s,%6s)		[ OK ] " %(a[i],b[i]))

	def test_subtraction(self):
		"""
		Tests the correct functionality of the Subtraction function
		"""
		print(".....Subtraction Tests......")
		a = [1,1,2,-1,0.5,1.5,-0.5,1E42,1,1]
		b = [1,0,-2,-2,0.5,0.25,-0.75,1E42,1E-1,-1E-1]
		expectedResult = [0,1,4,1,0,1.25,0.25,0,0.9,1.1]
		for i in range(0,len(a)):
			result = calc.Subtraction(a[i],b[i])
			if not self.assertEqual(expectedResult[i],result):
				print("--TEST-- Subtraction(%6s,%6s)		[ OK ]" %(a[i],b[i]))

	def test_division(self):
		"""
		Test the correct functionality of the Division function
		"""
		print(".....Division Tests......")
		a = [0,1,1,1E42,-0,-1,-1,-1E42,1.5,-0.25]
		b = [5,1,0.5,2,1,1,-2,1E42,2,-0.4]
		expectedResult = [0,1,2,5E41,0,-1,0.5,-1,0.75,0.625]
		for i in range(0,len(a)):
			result = calc.Division(a[i],b[i])
			if not self.assertEqual(expectedResult[i],result):
				print("--TEST-- Division(%6s,%6s)		[ OK ]" %(a[i],b[i]))
		SpecialA = [1,0]
		SpecialB = [0,0]
		for i in range(0,len(SpecialA)):
			if not self.assertIsNone(calc.Division(SpecialA[i],SpecialB[i])):
				print("--TEST-- Division(%6s,%6s)		[ OK ]" %(a[i],b[i]))

	def test_multiplication(self):
		"""
		Tests the correct functionality of the Mulitplication function
		"""
		print(".....Mulitplication Tests......")
		a = [0,1,42,1E42,-0,-1,-42,-1E42,0.5,-0.5]
		b = [1,42,42,42,1,-42,42,42,2,2]
		expectedResult = [0,42,1764,42E42,0,42,-1764,-42E42,1,-1]
		for i in range(0,len(a)):
			result = calc.Multiplication(a[i],b[i])
			if not self.assertEqual(expectedResult[i],result):
				print("--TEST-- Mulitplication(%6s,%6s)		[ OK ]" %(a[i],b[i]))

	def test_factorial(self):
		"""
		Tests the correct functionality of the Factorial function
		"""
		print(".....Factorial Tests......")
		a = [0,2]
		expectedResult = [1,2]
		for i in range(0,len(a)):
			result = calc.Factorial(a[i])
			if not self.assertEqual(expectedResult[i],result):
				print("--TEST-- Factorial(%6s)			[ OK ]" %(a[i]))
		SpecialA = [-1,0.1,1E-5,1.2]
		for i in range(0,len(a)):
			if not self.assertIsNone(calc.Factorial(SpecialA[i])):
				print("--TEST-- Factorial(%6s)			[ OK ]" %(a[i]))

	def test_exponentiation(self):
		"""
		Test the correct functionality of the Exponentiation function
		"""
		print(".....Exponentiation Tests......")
		a = [0,1,1E21,2,-5,-2,2]
		b = [2,2,2,-1,2,3,0.1]
		expectedResult = [0,1,1E42,0.5,25,-8,1.0717734625362931]
		for i in range(0,len(a)):
			result = calc.Exponentiation(a[i],b[i])
			if not self.assertEqual(expectedResult[i],result):
				print("--TEST-- Exponentiation(%6s,%6s)		[ OK ]" %(a[i],b[i]))

	def test_root(self):
		"""
		Test the correct functionality of the Root function
		"""
		print(".....Root Tests......")
		a = [0,1,8,8,1E42]
		b = [42,42,3,-3,2]
		expectedResult = [0,1,2,0.5,1E21]
		for i in range(0,len(a)):
			result = calc.Root(a[i],b[i])
			if not self.assertEqual(expectedResult[i],result):
				print("--TEST-- Root(%6s,%6s)			[ OK ]" %(a[i],b[i]))

		SpecialA = [-1,-1E42]
		SpecialB = [2,2]
		for i in range(0,len(SpecialA)):
			if not self.assertIsNone(calc.Root(SpecialA[i],SpecialB[i])):
				print("--TEST-- Root(%6s,%6s)			[ OK ]" %(a[i],b[i]))

	def test_log(self):
		"""
		Test the correct functionality of the Log function
		"""
		print(".....Log Tests......")
		a = [1,42,100,1E42]
		b = [5,42,10,1E21]
		expectedResult = [1,1,2,2]
		for i in range(0,len(a)):
			result = calc.Log(a[i],b[i])
			if not self.assertEqual(expectedResult[i],result):
				print("--TEST-- Log(%6s,%6s)		[ OK ]" %(a[i],b[i]))

		SpecialA = [0,-1,1,-1E42]
		SpecialB = [5,2,-1,-1E42]
		for i in range(0,len(SpecialA)):
			calc.Log(SpecialA[i],SpecialB[i])
			if not self.assertIsNone(calc.Log(SpecialA[i],SpecialB[i])):
				print("--TEST-- Log(%6s,%6s)		[ OK ]" %(a[i],b[i]))


if __name__ == '__main__':
	unittest.main()