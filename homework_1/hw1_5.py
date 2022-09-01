n=1
x=0
y=1
print ("Value number 0 is 0")
while n<=50:
    print("Value number", n, "is", end=" ")
    n = n + 1
    temp = x
    x = y
    y = x + temp
    print (y)
