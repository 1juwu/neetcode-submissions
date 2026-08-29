class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. 建立一個 dp 陣列，長度為 amount + 1
        # 預設值填入 amount + 1（因為硬幣最小是 1 元，不可能有任何金額的硬幣數會大於 amount + 1，這用來代表「無限大」）
        dp = [amount + 1] * (amount + 1)

        # 2. 基本狀態：湊齊 0 元需要 0 個硬幣
        dp[0] = 0

        # 3. 外層迴圈：從 1 元一路算到目標金額
        for i in range(1, amount + 1):
            # 內層迴圈：檢查手上的每一種硬幣
            for coin in coins:
                # 如果目前的金額「扣得掉」這枚硬幣
                if i - coin >= 0:
                    # 狀態轉移：比較「原本的方法 (dp[i])」與「拿了這枚硬幣的方法 (dp[i - coin] + 1)」哪個硬幣比較少？
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # 4. 如果 dp[amount] 依然是初始的無限大
        # 代表完全湊不出來，回傳 -1；否則回傳答案

        if dp[amount] <= amount:
            return dp[amount] 
        else:
            return -1