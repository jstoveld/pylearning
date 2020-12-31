import numpy as np
from datetime import datetime


def first_and_last(message):
  try:
    if message =='': return False
    if message == None: return False
    message = str(message)
    if len(message) <=1: True
    if message[0] == message[-1]: return True
    else:
        return False
  except:
    return False

# print(first_and_last())
print(first_and_last('a'))
print(first_and_last('Hello'))
print(first_and_last(""))
print(first_and_last(1))
print(first_and_last([]))
print(first_and_last("hello"))
# print(first_and_last(datetime.datetime(2020, 11, 26, 19, 28, 6, 864250)))