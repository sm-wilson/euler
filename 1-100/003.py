n = input("Enter an integer: ")
n = int(n)
print("Factors are: ")
i = 1
while i <= n:
    k = 0
    if n % i == 0:
        j = 1
        while j <= i:
            if i % j == 0:
                k = k + 1
            j = j + 1
        if k == 2:
            print(i)
            pass
    i = i + 1
