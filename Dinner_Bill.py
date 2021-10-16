# Programmer: David Yue
# Date: 10/14/21
# Module for connecting all the different function

from appitizer import *
from entree import *
from dessert import *

def main():
    appitizer_cost = appitizer_function()
    entree_cost = entree_function()
    dessert_cost = dessert_function ()
    total = appitizer_cost + entree_cost + dessert_cost
    print(f'Your total cost is ${total:.2f}')

if __name__ == '__main__':
    main()