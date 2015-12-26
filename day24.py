a = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
     113]

s = sum(a)
gsize = s // 4
inf = len(a) * 2

dp = [inf for i in range(s + 1)]
last = [[] for i in range(s + 1)]
dp[0] = 0

for i in range(len(a)):
    for j in range(len(dp) - 1, -1, -1):
        if j + a[i] < len(dp):
            if dp[j + a[i]] >= dp[j] + 1:
                nw = last[j] + [i]
                m1 = 1
                m2 = 1
                for z in nw:
                    m1 *= a[z]
                for z in last[j + a[i]]:
                    m2 *= a[z]
                if m1 < m2 or dp[j + a[i]] > dp[j] + 1:
                    dp[j + a[i]] = dp[j] + 1
                    last[j + a[i]] = nw

print (gsize)
print(last[gsize])
m = 1
_sum = 0
for i in last[gsize]:
    m *= a[i]
    _sum += a[i]

print (m, _sum)
