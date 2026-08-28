class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)

        # 基底條件：1 階只有 1 種方法，2 階有 2 種方法
        if n <= 2:
            return n
        
        # one 代表 f(n-2)，two 代表 f(n-1)
        # 一開始分別代表第 1 階和第 2 階 的方法數
        one, two = 1, 2
        
        # 從第 3 階一路算到第 n 階
        for i in range(3, n + 1):
            # 當前這一階的方法數 = 前兩階相加
            current = one + two
            
            # 關鍵接力（滾動更新）：
            # 原本的 f(n-1) 變成下一輪的 f(n-2)
            # 原本的 current 變成下一輪的 f(n-1)
            one = two
            two = current
            
        return two

        


    
        