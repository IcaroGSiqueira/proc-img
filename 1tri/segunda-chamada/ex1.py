N=10

def fat_loop(n):
    result = 1 if n > 0 else True
    for i in range(1, n+1):
        result = result * i
    return result

def fat_recursive(n):
    return True if (n == 0) else n * fat_recursive(n-1)

print("Loop:\t\t", fat_loop(N))

print("Recursivo:\t", fat_recursive(N))