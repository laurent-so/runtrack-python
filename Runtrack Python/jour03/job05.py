primes = [True] * 1000
primes[0] = False
primes[1] = False
for i in range(2, int(1000 ** 0.5) + 1):
  if primes[i]:
    for j in range(i ** 2, 1000, i):
      primes[j] = False
for i in range(1000):
  if primes[i]:
    print(i + 1)