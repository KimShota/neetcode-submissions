class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        maxLength = 1
        left = 0
        right = 1
        hashSet = set()

        while right < n:
            hashSet.add(s[left])
            if s[right] not in hashSet:
                maxLength = max(maxLength, right - left + 1)
                hashSet.add(s[right])
                right += 1
            else:
                if left == right:
                    right += 1
                else:
                    hashSet.remove(s[left])
                    left += 1
                    hashSet.add(s[left])

        return maxLength 