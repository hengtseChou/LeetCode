class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Take coins=[1,2,5] and amount = 11 as an example,
        # If I use one 1, I need to know the fewest number of coins I need to make up 10, i.e., dp[10]. Overall I need 1+dp[10] coins.
        # If I use one 2, I need 1+dp[9] coins.
        # If I use one 5, I need 1+dp[6] coins.
        # Therefore, I need to calculate dp from 1 to amount.

        # ref: https://emmielin.medium.com/leetcode-%E7%AD%86%E8%A8%98-322-coin-change-d2a7acdbaaec

        if amount == 0:
            return 0

        dp = [amount + 1] * (amount + 1)  # default to impossible value
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin:  # coin is larger than current amount, skip the iteration
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] > amount:
            return -1
        return dp[amount]
