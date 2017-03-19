data = [[1, 2], [3, 4, 5], [20, 30]]

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def pro(data, index=0, a=0, b=0, c=0):
    if index < len(data):
        for i in data[index]:
            k = index_2d(data, i)[0]
            if k == 0:
                a = i
            elif k == 1:
                b = i
            else:
                c = i
            pro(data, index + 1, a, b, c)
    else:
        print a, b, c


pro(data)