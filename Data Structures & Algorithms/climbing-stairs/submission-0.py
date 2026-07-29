class Solution:
    def climbStairs(self, n: int) -> int:
        memoize = [None for _ in range(n)]
        return self.dp(0, n, memoize)

    def dp(self, i, n, memoize):
        if i == n:
            return 1
        if i > n:
            return 0
        if memoize[i] is not None:
            return memoize[i]
        memoize[i] =self.dp(i+1, n, memoize) + self.dp(i+2, n, memoize)
        return memoize[i]

        