"""HorizontalHistogram"""
def check(text):
    """ show frequency """
    new_lst = sorted(set([i for i in text]))
    for i in new_lst:
        if i == i.lower():
            print_(i, text)
    for i in new_lst:
        if i != i.lower():
            print_(i, text)

def print_(index, text):
    print(index,": ", end="")
    print(index)
    count = text.count(index)
    for j in range(1, count+1):
        print(j, count)
        if j > 0:
            print("-", end="")
        elif j%5 == 0:
            print("|", end="")
    print('')

check(input())
