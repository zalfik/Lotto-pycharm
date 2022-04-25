import random


# Class of coupons
class Lottery:
    def __init__(self, date):
        # Attribute date will be used later... For now, it's just a number/id
        self.date = date
        self.single_draw = []

    # Fill a coupon with random numbers
    def fill(self):
        numbers_per_draw = 6
        numbers_range = 49
        while len(self.single_draw) < numbers_per_draw:
            number = random.randint(1, numbers_range)
            if number not in self.single_draw:
                self.single_draw.append(number)
        self.single_draw.sort()


# Create a dictionary of >number< draws. Adds new draws if not empty.
def multidraw(draw_dict, number):
    for i in range(len(draw_dict) + 1, len(draw_dict) + number + 1):
        one_draw = Lottery(i)
        one_draw.fill()
        draw_dict[i] = one_draw.single_draw


# Count hits in drawn from coupon
def count_hits(drawn, coupon):
    hits = 0
    for item in coupon:
        if item in drawn:
            hits += 1
    return hits


# Create a dictionary where key is number of hits and value is a list of lottery numbers
def make_hits_dict(draws_set, coupon):
    hits_dict = {number: [] for number in ['0', '1', '2', '3', '4', '5', '6']}
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


