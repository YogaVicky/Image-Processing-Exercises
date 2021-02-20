import math
a = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def max(a):
    r = a[0][0]
    for i in a:
        for j in i:
            if j > r:
                r = j
    return r


def sum(a):
    r = 0
    for i in a:
        for j in i:
            r = r + j
    return r


def mean(a):
    r = sum(a)
    t = len(a)*len(a[0])
    r = r/t
    return r


def median(a):
    t = []
    for i in a:
        for j in i:
            t.append(j)
    t.sort()
    s = 0
    if len(t) % 2 == 0:
        s = len(t)/2
        s = int(s)
        r = (t[s-1]+t[s])/2

    else:
        s = (len(t)-1)/2
        s = int(s)
        r = t[s]
    return r


def mode(a):
    t = {}
    for i in a:
        for j in i:
            if j not in t:
                t[j] = 1
            else:
                t[j] = t[j]+1
    s = 2
    r = []
    for i in t:
        if t[i] > s:
            r.clear()
            r.append(i)
        if t[i] == s:
            r.append(i)
    return r


def std_deviation(a):
    t = mean(a)
    p = 0
    for i in a:
        for j in i:
            p = p+((j-t)*(j-t))
    s = len(a)*len(a[0])
    r = math.sqrt(p/s)
    return r


def freq_distr(a):
    t = {}
    for i in a:
        for j in i:
            if j not in t:
                t[j] = 1
            else:
                t[j] = t[j]+1
    return t


# print(median(a))
# print(sum(a))
# print(mean(a))
#k = mode(a)
# print(k)
#print("hi ")
# print(std_deviation(a))
#t = freq_distr(a)
# print(t)
