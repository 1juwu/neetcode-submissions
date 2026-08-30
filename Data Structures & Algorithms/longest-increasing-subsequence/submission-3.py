class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i] 表示以 nums[i] 結尾的最長遞增子序列長度
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                # 只要前面的數字比當前數字小，就可以接在後面
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        # 答案是所有結尾中最長的那個
        return max(dp)
        