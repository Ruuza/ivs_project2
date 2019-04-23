
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import calculator.calc_lib as calc


def stDev(file):
    """
    **Stadandard Deviation:**
    Calculates the standard deviation of numbers input through stdin.

    :param file: stdin input

    :type file: string
      
    :return: Value of the standard deviation    

    """
    total = 0
    totalSquared = 0
    numbers = []
    for line in file:
        numbers.append(line.rstrip())
    N = len(numbers)

    for number in numbers:
        total = calc.Addition(total,float(number))
        totalSquared = calc.Addition(totalSquared,calc.Exponentiation(float(number),2))
    average = calc.Division(total,N)
    stdDevAverage = calc.Multiplication(N,calc.Exponentiation(average,2))
    stdDev = calc.Root(calc.Division(calc.Subtraction(totalSquared,stdDevAverage),N-1),2)
    print("------STANDARD DEVIATION------")
    print(stdDev)
    return None


