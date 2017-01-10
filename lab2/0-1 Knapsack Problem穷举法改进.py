bestV = 0
curW = 0
curV = 0
bestx = None
call = 0


def backtrack(i):
    global bestV, curW, curV, x, bestx, call
    call += 1
    if i >= n:
        if bestV < curV:
            bestV = curV
            bestx = x[:]
            print bestx
    else:
        if curW + w[i] <= c:
            x[i] = True
            curW += w[i]
            curV += v[i]
            backtrack(i + 1)
            curW -= w[i]
            curV -= v[i]
        x[i] = False
        backtrack(i + 1)


if __name__ == '__main__':
    n = 4
    c = 10
    w = [2, 3, 4, 7]
    v = [1, 3, 5, 9]
    x = [False for i in range(n)]
    backtrack(0)
    print(bestV)
    print(bestx)
    print "call = ",call