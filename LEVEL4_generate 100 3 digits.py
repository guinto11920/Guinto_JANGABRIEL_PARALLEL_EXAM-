import random

res = [random.randrange(1,999, 1) for i in range(101)]

nine= []
prime = []
evenlist = []
oddlist = []
divisible =[]
for i in res:
   if (i % 2 == 0):
      evenlist.append(i)
   else:
        oddlist.append(i)

print("All element in the list : " + str(res))
print("Even lists:", evenlist)
print("Odd lists:", oddlist)

for i in res:
   if (i % 9 == 0):
      divisible.append(i)
print("Divisible by 9", divisible)

def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

for n in res:
    if is_prime(n):
        if n==97:
            prime.append(n)
        else:
            prime.append(n)

print("Prime numbers", prime)

n = 9
for i in res:
    if i % 10 == 9:
        nine.append(i)
print("Contains number 9 :", nine)
