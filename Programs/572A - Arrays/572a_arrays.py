# Description of the problem can be found at http://codeforces.com/problemset/problem/572/A

na, nb = map(int, input().split())
k, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A[k - 1] >= B[len(B) - m]:
    print("NO")
else:
    print("YES")
    