
a = []

def fibonaci(length):
    x = 1
    for i in range(0, length):
        if i < 2:
            x = 1
        else: x = a[i-2]+a[i-1]
        a.append(x)
    print(a)

fibonaci(20)