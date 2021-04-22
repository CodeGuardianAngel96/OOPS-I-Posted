'''
    Write a class with name Calculate. 
    It contains a method called product() which contains three parameters a , b, c. 
    The default values of all parameters are 1.
    This method calculates the product of three parameters.
    Overload the function during function call.
'''

class Calculate:

    def __init__(self):

        pass

    def product(self, a = 1, b = 1, c = 1):

        return a * b * c

if __name__ == "__main__":

    calc = Calculate()

    result1 = calc.product(43)
    result2 = calc.product(23, 3)
    result3 = calc.product(10, 12, 2)
    print("single parameter: ", result1)
    print("double parameter: ", result2)
    print("triple parameter: ", result3)