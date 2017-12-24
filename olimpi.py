w, h = 3,3
Matrix = [[0 for x in range(w)] for y in range(h)]

for num in xrange(1, w+1):
    for row in xrange(0, w):
        if row+1 == num:
            continue
        else:
            rowable = True
            for k in Matrix[row]:
                if k != 0:
                    rowable = False
                    break
            if rowable:
                for col in xrange(0, w):
                    if col+1 == num:
                        continue
                    else:
                        Matrix[row][col] = num
                        print "**************"
                        for c in Matrix:
                            print c
                        Matrix = [[0 for x in range(w)] for y in range(h)]


