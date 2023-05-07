def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n, x):
    primes = []
    for i in range(n, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes

n = int(input("Введите начало диапазона: "))
x = int(input("Введите конец диапазона: "))
primes = get_primes(n, x)
print("Простые числа от", n, "до", x, ":", primes)