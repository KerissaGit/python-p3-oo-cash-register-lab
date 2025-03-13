#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0, items = None, last_transaction = 0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_transaction = 0
  
  def add_item(self, name, price, quantity = 1):
    for i in range(quantity):
      self.items.append(name)
    
    self.last_transaction = price * quantity
    self.total += price * quantity
  
  def apply_discount(self, discount = 0.00):
    if self.discount > 0:
        self.total *= (1 - self.discount / 100)
        print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def new_register(self, new_item, price, quantity = 1):
    for i in range(quantity):
      self.items.append(new_item)
  
  def void_last_transaction(self):
    self.total -= self.last_transaction


    