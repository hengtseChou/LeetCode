class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        # ref: https://www.geeksforgeeks.org/generate-all-numbers-up-to-n-in-lexicographical-order/
        # ref: https://assets.leetcode.com/users/images/c6aa8a16-9df8-4a19-8b9c-cf9755ea1082_1716309559.368739.jpeg

        def dfs(x, n, ans):
            if x > n:
                return
            ans.append(x)
            dfs(x * 10, n, ans)
            if x % 10 != 9:
                dfs(x + 1, n, ans)

        ans = []
        dfs(1, n, ans)
        return ans
