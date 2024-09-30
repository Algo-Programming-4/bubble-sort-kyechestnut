lis = [10000, 5, 8, 11, 12, 5, 12, 18, 200, 1, 7]

def bubble (lis, length):
    while length > 0:
        itterations =0
        x = 0
        while x < length:
            if lis[x] > lis[x+1]:
                nw = lis[x]
                lis[x] = lis[x+1]
                lis[x+1] = nw
            x+=1
            itterations +=1
        length-=1
        print(itterations)
        print(lis)
        
    print(x)
    return lis




aList = bubble(lis, len(lis)-1)
print (aList)
