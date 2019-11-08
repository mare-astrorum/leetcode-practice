MINIMUM NUMBER OF CHAIRS

starts = [1, 2, 6, 5, 3]
ends = [5, 5, 7, 6, 8]


def cal_chairs(starts, ends):
    all = [(s, 1) for s in starts] + [(e, -1) for e in ends]
    all = sorted(all)
    num = 0
    largest = 0
    for pos, t in all:
        num += t
        if largest < num:
            largest = num
    return largest
