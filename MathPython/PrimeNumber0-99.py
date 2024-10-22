def ispraime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
    
def list_primes():
    for n in range(100):
        if ispraime(n):
            print(n, end=' ', flush=True)
    print()

list_primes()
