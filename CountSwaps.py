
counter = 0

def msort(x):
    result = [0]*len(x)
    if len(x) < 2:
        return x,0
    mid = int(len(x)/2)
    y= msort(x[:mid])
    z= msort(x[mid:])

    print ('x=', x,'y=', y,'z=', z, 'counter=', counter)
    yl = len(y)
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
                counter = counter + len(y)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)          
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result


T = int(input())
for i in range(T):
    N = int(input())
    a = [int(x) for x in input().strip().split()]
    res = msort(a)
    print (counter)
