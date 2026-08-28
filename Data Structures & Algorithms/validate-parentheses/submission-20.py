class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        # 用字典建立右括號與對應左括號的映射關係 {Key: Value}
        mapping = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in mapping:  # 看是否為')', '}', ']'
                # 堆疊為空
                # 頂端括號(.pop就是將stack最上面的字母拿出來)不匹配
                if not stack or stack.pop() != mapping[char]:
                    return False
            # 如果是左括號，直接推入堆疊
            else: # "(", "{", "["
                stack.append(char)

        # 走訪結束後，堆疊為空才算完全匹配成功
        return not stack
        