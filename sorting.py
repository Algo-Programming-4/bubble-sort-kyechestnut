
def bubble (lis):
    length = len(lis)
    while length > 0:
        itterations =0
        x = 1
        while x < length:
            if lis[x] < lis[x-1]:
                nw = lis[x]
                lis[x] = lis[x-1]
                lis[x-1] = nw
            x+=1
            itterations +=1
        length-=1
    print(x)
    return lis

