memo = {}

def climb_stairs(n):
    if n in (1, 2):
        return n

    if n in memo:
        return memo[n]

    ans = climb_stairs(n-1) + climb_stairs(n-2)

    memo[n] = ans
    return ans


climb_stairs(10)


