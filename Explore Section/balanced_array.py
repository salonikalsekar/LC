from collections import defaultdict
def pointPuzz(elements):
    c = defaultdict(int)
    res = 0
    for num in elements:
        c.setdefault(num, 0)
        c[num] += num
        res = max(num, res)

    points = [0] * (res + 1)
    dp = [0] * (res + 2)
    for k, v in c.items():
        points[k] = v

    result = 0
    for i in range(len(points)):
        if i == 0:
            dp[i+1] = points[i]
        else:
            dp[i+1] = max(dp[i], dp[i-1] + points[i])
        result = max(dp[i+1], result)
    return result

print(pointPuzz([5,6,6,4,11]))
