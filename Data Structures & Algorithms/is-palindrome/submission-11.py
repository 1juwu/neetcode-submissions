class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[\s,?!.\':]', "", s)
        same = 0

        for i in range(len(s)//2):
            if s[i] == s[len(s)-i-1]:
                same += 1

        if same == len(s)//2:
            return True
        else:
            return False
        