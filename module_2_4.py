#Всё не так уж просто

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # список только из простых чисел
not_primes = [] # список без простых чисел
is_prime = True

for i in range(len(numbers)):
    for k in range(2, numbers[i], 1):
        if numbers[i] % k != 0:
            primes [i] = numbers[i] % k
            print(primes)