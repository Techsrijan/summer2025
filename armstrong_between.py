for n in range(100,1000):
    orig = n
    sum = 0
    while n > 0:
        a = n % 10
        sum = sum + a * a * a
        n = n // 10

    if sum == orig:
        print("Armstrong no=",orig)
