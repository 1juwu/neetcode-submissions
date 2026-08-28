class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
       
        nums = sorted(list(set(nums)))
        ans = 1
        # print(sorted(nums))
        
        max_ans = 1

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                ans += 1
                if ans > max_ans:
                    max_ans = ans

            elif nums[i+1] - nums[i] != 1:
                if ans > max_ans:
                    max_ans = ans
                ans = 1
            # print(ans, max_ans)
        return max_ans
