def caching_fibonacci():
    """
    Returns a Fibonacci function with caching capability.
    
    Usage:
        - fib = caching_fibonacci()
        - print(fib(10))  # Outputs 55
        - print(fib(15))  # Outputs 610
    """
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci