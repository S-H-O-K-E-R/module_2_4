numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = False
for i in numbers:
    for j in range(2, i):
      if i % j == 0:
        a = True
        break
      else:
            a = False
    if a == True:
        not_primes.append(i)
    elif i != 1 and a == False:
        primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)