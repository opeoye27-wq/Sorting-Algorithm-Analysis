def move_five_percent_front(L: list):
    percent = int((len(L)) * .05)
    moved = 0
    while moved != percent:
        L.insert(0, L[len(L) - 1])
        L.pop()
        moved += 1
    return L

def move_five_percent_end(L: list):
    percent = int((len(L)) * .05)
    moved = 0
    while moved != percent:
        L.append(L[0])
        L.pop(0)
        moved += 1
    return L

def reverse_order(L):
    return L[::-1]
