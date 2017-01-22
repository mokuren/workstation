'''
Fraction operation
'''

from fractions import Fraction

def add(a, b):
    print("{0} + {1} = {2}".format(a, b, a+b))

def Substract(a, b):
    print("{0} - {1} = {2}".format(a, b, a-b))

def Divide(a, b):
    print("{0} / {1} = {2}".format(a, b, a/b))

def Multiply(a, b):
    print("{0} * {1} = {2}".format(a, b, a*b))


if __name__ == '__main__':

    while True:
        a = Fraction(input('Enter first Fraction:'))
        b = Fraction(input('Enter second Fraction:'))
        op = input('AD, Substract, Divide, Mulitiply:')
        if op == 'AD':
            add(a, b)
        if op == 'Substract':
            Substract(a, b)
        if op == 'Divide':
            Divide(a, b)
        if op == 'Multiply':
            Multiply(a, b)

        ans = input('Want u Break? y/n ?')
        if ans == 'y':
            break
