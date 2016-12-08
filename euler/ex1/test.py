
print("Hello")

"""generate a list of all numbers below 1000
pull out all multiples of 3
pull out all multiples of 5
only add in multiples of 15 once
sum that new list"""
range(1000) #generates all numbers below n generator list - can only traverse
max = 1000
x = []

for i in range(max):
    if i%3 == 0:
        x.append(i)
    if (i%5 == 0) and (i%3 != 0):
        x.append(i)

print(sum(x))


