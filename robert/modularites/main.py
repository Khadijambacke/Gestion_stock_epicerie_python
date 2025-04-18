#from math_util import *
#resultat = addition(5,7)
#res = soustraction(8,7)
#print(f"la somme est:{resultat}")
from base64 import decode
def momo(function):
    def nin() :
        print("debut d'execution")
        function()
        print("fin d'execution")
    return nin
@momo
def safar():
    print("atender")
safar()
def division_secure(a, b) :
    try:
        a=int(input("donnez la valeur de a"))
        b=int(input("donnez la valeur de b"))
        div=a/b
        print("cest bon")
    except ZeroDivisionError:
        print("none")
division_secure(1,0)