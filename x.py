import sys
from bisect import bisect_left, bisect_right
data = sys.stdin.buffer.read().split()
rl = iter(data)
N, Q = int(next(rl)), int(next(rl))
A = [int(next(rl)) for _ in range(N)]

ans = []
for _ in range(Q):
    X = int(next(rl))
    l = bisect_left(A, X)
    r = bisect_right(A, X)
    ans.append("-1 -1" if l == N or A[l] != X else f"{l+1} {r}")

sys.stdout.write("\n".join(ans))

# import sys
# from bisect import bisect_left, bisect_right

# # Leer todo de una sola vez (ultra rápido)
# data = sys.stdin.buffer.read().split()
# it = iter(data)

# N = int(next(it))
# Q = int(next(it))
# A = [int(next(it)) for _ in range(N)]

# out = []
# for _ in range(Q):
#     X = int(next(it))
#     l = bisect_left(A, X)
#     if l == N or A[l] != X:
#         out.append(b"-1 -1")
#     else:
#         r = bisect_right(A, X)
#         # Evitar f-string, convertir a bytes directamente
#         out.append(f"{l+1} {r}".encode())

# # Salida final: unir por '\n'
# sys.stdout.buffer.write(b"\n".join(out))

import sys
from bisect import bisect_left, bisect_right
rl = sys.stdin.readline

N, Q = map(int, rl().split())
A = list(map(int, rl().split()))

ans = []
for _ in range(Q):
    X = int(rl())
    l = bisect_left(A, X)
    r = bisect_right(A, X)
    ans.append("-1 -1" if l == N or A[l] != X else f"{l+1} {r}")

sys.stdout.write("\n".join(ans))