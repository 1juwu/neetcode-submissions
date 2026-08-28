class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        same = 0
        for i in range(min(len(s), len(t))):
            if s[i] == t[i]:
                same += 1
        if same == max(len(t), len(s)):
            return True
        else:
            return False