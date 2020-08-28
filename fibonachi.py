def fibonachi(a):
    f = 0
    s = 1
    print(f, s, end=" ")
    for x in range(a):
        next = f + s
        print(next, end=" ")
        f = s
        s = next
