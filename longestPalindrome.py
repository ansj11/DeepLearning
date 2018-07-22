class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        left = 0
        right = l-1
        while left<right:
            head = left
            tail = right
            mid = round((head + tail)/2)
            for i in range(0, mid-head):
                if s[head+i] == s[tail-i]:
                    continue
                elif s[left] ==s[right-1]:
                    right -= 1
                    break
                elif s[right] == s[left+1]:
                    left += 1
                    break
            else:
                return s[left:right]
