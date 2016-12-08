x = [1,2] #put in Fibonacci numbers using a for loop by summing (i) + (i + 1)

for i in x:
    x.append(sum(x+(x+1)))
    print(x)

