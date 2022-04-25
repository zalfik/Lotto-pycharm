from utilities import multidraw, make_hits_dict, your_results


my_coupon = [7, 18, 22, 26, 33, 49]
draws_set = {}

print(f'Hello! This is your coupon: {my_coupon}')
how_many = int(input('How many draws do you wanna make?\n'))

multidraw(draws_set, how_many)
print(draws_set)
print('===========================================================')
hits_dict = make_hits_dict(draws_set, my_coupon)
print(your_results(hits_dict))


