class Solution:
    def rob(self, nums: List[int]) -> int:
        # 上一題的解法變成函數

        def rob_linear(nums):
            n = len(nums)
            # 1. 建立 DP 帳本
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            # 2. 依序推導每一格（二選一：不偷今天 vs 偷今天+前天）
            for i in range(2, n):
                dp[i] = max(dp[i-1], nums[i] + dp[i - 2])

             # 3. 回傳這條街的最大金額
            return dp[n-1]

        # 正題
        n = len(nums)

        # 基礎防錯：如果只有 1 間房，直接偷它
        if n == 1:
            return nums[0]

        # 基礎防錯：如果只有 2 間房，挑大的偷
        if n == 2:
            return max(nums[0], nums[1])

        # 呼叫我們熟悉的 House Robber I 直線解法
        # 情境 A：去掉最後一間房子
        case_A = rob_linear(nums[:-1])
        # 情境 B：去掉第一間房子
        case_B = rob_linear(nums[1:])

        return max(case_A, case_B)


        