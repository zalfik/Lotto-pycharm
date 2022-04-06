# import random

from utilities import multidraw

my_coupon = [7, 18, 22, 26, 33, 49]
draws_set = {}
how_many = 0

print('Hello! This is your coupon: ', my_coupon)
how_many = int(input('How many draws do you wanna make?\n'))

multidraw(draws_set, how_many)
print(draws_set)