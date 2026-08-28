class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        ttl = 1
        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                ttl = ttl * nums[i]  
            else:
                zero += 1 #計算有幾個 0
        # print(zero, ttl)
        
        if zero == 0: # 沒有 0
            for i in range(len(nums)):
                ans.append(round(ttl/nums[i]))
        elif zero >= 2: 
            for i in range(len(nums)):
                ans.append(0)
        else: # 有0
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans.append(ttl)
                else:
                    ans.append(0)
        #print(ans, ttl)
        return ans
            
