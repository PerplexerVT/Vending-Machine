
#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    num_items = 0
    item_price = 0
    def __init__(self, n_i, i_p):
        self.num_items = n_i #total item count
        self.item_price = i_p #single item price
    def buy(self, r_i, m):
        cost = self.item_price * r_i #items total price
        if r_i <= self.num_items: #checks stock
            if m >= cost: #checks money vs total price
                self.num_items -= r_i #removes from stock
                return int(m - cost) #returns change
            else:
                 return "Not enough coins"
        else:
            return "Not enough items in the machine"
    pass
if __name__ == '__main__':
    fptr = sys.stdout
    print("input number of items, then item price")
    print("example with 20 items costing 4 each: 20 4")
    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)
    
    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
