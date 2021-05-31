from mathematics.numbers import Binomial

m, n = map(int, input().split())
print(Binomial(m + n, m))