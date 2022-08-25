from sympy import *

def harmonic(n):
    if n<2:
        return 1
    else:
        return 1/n + (harmonic(n-1))
if __name__=='__main__':
    n=int(input("Enter the no."))
    nth_harmonic = harmonic(n)
    print("Value of nth harmonic number : {}".format(nth_harmonic))