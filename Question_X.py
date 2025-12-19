# X. Two intervals
l1, r1, l2, r2 = map(int, input().split())

if max(l1, l2) <= min(r1, r2):
    print(max(l1, l2), min(r1, r2))
else:
    print(-1)
