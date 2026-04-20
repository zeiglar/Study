 # https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        hashmap = {}
        left = 0

        for right in range(len(s)):
            if(s[right] in hashmap and hashmap[s[right]] >= left):
                left = hashmap[s[right]] + 1
            
            hashmap[s[right]] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength