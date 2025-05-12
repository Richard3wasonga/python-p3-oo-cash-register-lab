#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction_amount = 0
   
  def add_item(self,title,price,quantity = 1):
    transaction_total = price * quantity
    self.total += transaction_total
    self.items.extend([title] * quantity)
    self.last_transaction_amount = transaction_total

  def apply_discount(self):
    if self.discount > 0:
      discount_amount = self.total * (self.discount/100)
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${int(self.total)}.")

    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction_amount
    self.last_transaction_amount = 0

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self,new_discount):
    self._discount = new_discount

 
cash_register = CashRegister(20)