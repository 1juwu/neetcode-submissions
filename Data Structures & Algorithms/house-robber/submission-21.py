class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]

        dp = len(nums) * [0] # 代表偷到第幾間時最多可以拿到的錢
        # max_rob = 0
        rob = 0

        for i in range(len(nums)):
            if i < 2: # 如果小於2(0, 1)
                dp[i] = nums[i]
            else: # i >= 2
                for j in range(i-2, -1, -1):
                    if max(nums[i] + dp[j], dp[i-1]) >= dp[i]:
                        dp[i] = max(nums[i] + dp[j], dp[i-1])
                        #print(i, j, nums[i], nums[j])

        #print(dp)
        return dp[len(nums)-1]
                








