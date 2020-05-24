def is_prim(N):
    return [x for x in range(2, N) if not [t for t in range(2, x) if not x % t]]


def is_prim2(N):
    return (x for x in range(2, N) if not [t for t in range(2, x) if not x % t])


def primefactors(N):
    return [x for x in is_prim(N)if N % x == 0]


def primefactors2(N):
    return (x for x in is_prim(N)if N % x == 0)


def print_prime_factors_twoway(N):
    print(primefactors(N))
    print(list(primefactors2(N)))

print_prime_factors_twoway(554)