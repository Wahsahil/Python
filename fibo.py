a = 0
b = 1
n = int(input("Enter how many Fibonacci numbers you want: "))
count = 0
while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1