class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = -1
        end = -1
        letterDict = {}
        maxLength = 0
        
        for end in range(len(s)):
            if s[end] in letterDict:
                maxLength = max(maxLength, end - start - 1)
                start = letterDict[s[end]]
                letterDict = {k:v for k,v in letterDict.iteritems() if v >= start}
            letterDict[s[end]] = end
            # print start, end, letterDict, maxLength
        
        maxLength = max(maxLength, end - start)
        return maxLength
