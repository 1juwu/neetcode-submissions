class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {} # 創建一個記數的字典
        left = 0
        max_count = 0
        max_len = 0

        for right in range(len(s)):
            # 1. 累加當前字元計數，並記錄在字典裏面
            count[s[right]] = count.get(s[right], 0) + 1
            # 2. 只比對「唯一有增加的那個字元」是否為最高頻率
            max_count = max(max_count, count[s[right]])

            # 3. (總長度) - (高頻字元數) = 需要被替換的數字 
            # 如果需要被替換的數字多於扣打，則縮減窗口
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1 # 最左邊的字元 s[left] 被踢出窗口
                left += 1 # 指標往前移動

            # 4. 若合法，則更新最大合法窗口長度
            max_len = max(max_len, right - left + 1)

        return max_len
            
