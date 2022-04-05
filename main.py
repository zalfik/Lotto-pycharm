import random

array, cupon = [], [7, 18, 22, 26, 33, 49]
hits, atmpts, cash_spent = 0, 0, 0


def fullfill (tab):
    while len(tab) < 6:
        x = random.randint(1, 49)
        if not tab.count(x):
            tab.append(x)


def verify (tab, kpn, hit):
    for i in kpn:
        if tab.count(i):
            hit += 1
    return hit


while hits < 3:
    hits = 0
    array.clear()
    fullfill(array)
    array.sort()
    print(array)
    verify(array, cupon, hits)
    hits = verify(array, cupon, hits)
    print("Number of hits: ", hits)
    atmpts += 1
    cash_spent += 3
print("Number of attempts: ", atmpts)
print("Cash spent:", cash_spent, "zł")
