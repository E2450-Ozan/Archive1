xx = ["A", "A", "A", "B", "C", "C", "A", "D", "D", "D", "D", "D"]
def majority_vote(lst):
    d = ''
    a = 0
    for i in lst:
        if lst.count(i) > a:
            a = lst.count(i)
            d = i
    return d
print("Winners is: " + majority_vote(xx))