import random


# Class of coupons
class Coupons:
    def __init__(self, date):
        # Attribute date will be used later... For now, it's just a number
        self.date = date
        self.single_draw = []

    # Fill a coupon with random numbers
    def fill_coupon(self):
        numbers_per_coupon = 6
        numbers_range = 49
        while len(self.single_draw) < numbers_per_coupon:
            number = random.randint(1, numbers_range)
            if not self.single_draw.count(number):
                self.single_draw.append(number)
        self.single_draw.sort()
# class Verifier(Coupons):
#     def __init__(self):
#         self.user_coupon = []


# Creates a dictionary of >number< draws.
def multidraw(coupon, number):
    for i in range(len(coupon) + 1, len(coupon) + number + 1):
        single_draw = Coupons(i)
        single_draw.fill_coupon()
        coupon[i] = single_draw.single_draw


def count_hits(drawn, chosen, hit):
    for i in chosen:
        if drawn.count(i):
            hit += 1
    return hit
