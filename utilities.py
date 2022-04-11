import random


# Class of coupons
class Lottery:
    def __init__(self, date):
        # Attribute date will be used later... For now, it's just a number
        self.date = date
        self.single_draw = []

    # Fills a coupon with random numbers
    def fill(self):
        numbers_per_draw = 6
        numbers_range = 49
        while len(self.single_draw) < numbers_per_draw:
            number = random.randint(1, numbers_range)
            if not self.single_draw.count(number):
                self.single_draw.append(number)
        self.single_draw.sort()


# Creates a dictionary of >number< draws. Adds new draws if not empty.
def multidraw(draw_dict, number):
    for i in range(len(draw_dict) + 1, len(draw_dict) + number + 1):
        single_draw = Lottery(i)
        single_draw.fill()
        draw_dict[i] = single_draw.single_draw


# Counts hits in drawn from coupon
def count_hits(drawn, coupon):
    hits = 0
    for i in coupon:
        if drawn.count(i):
            hits += 1
    return hits


# Creates a dictionary where key is number of hits and value is a list of lottery numbers
def make_hits_dict(draws_set, coupon):
    hits_dict = {
        '0': [],
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': []
    }
    for lottery_number in draws_set:
        hits = count_hits(draws_set[lottery_number], coupon)
        hits_dict[str(hits)].append(lottery_number)
    return hits_dict


def your_results(hits_dict):
    print(f'No hits in {len(hits_dict["0"])} draws\n'
          f'One hit in {len(hits_dict["1"])} draws\n'
          f'Two hits in {len(hits_dict["2"])} draws\n'
          f'Tree hits in {len(hits_dict["3"])} draws\n'
          f'Four hits in {len(hits_dict["4"])} draws\n'
          f'Five hits in {len(hits_dict["5"])} draws\n'
          f'Six hits in {len(hits_dict["6"])} draws\n')

