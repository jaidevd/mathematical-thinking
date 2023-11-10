def gcd(a, b):
    smaller, larger = min(a, b), max(a, b)
    while smaller > 0:
        larger -= smaller
        smaller, larger = min(smaller, larger), max(smaller, larger)
    return larger
