class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        last = None
        lastDict = {}
        for i in range(len(s)):
            # print lastDict
            tmpDict = {1: s[i]}
            if s[i] == last:
                tmpDict[2] = s[i] * 2
            for k in lastDict.keys():
                if (i-k-1 >=0) and (s[i] == s[i - k - 1]):
                    tmpDict[k + 2] = s[i-k-1:i+1]
                else:
                    if k > len(longest):
                        longest = lastDict[k]
            lastDict = tmpDict
            last = s[i]
        # print 'aaa', lastDict
        if lastDict:
            maxKey = max(lastDict.keys())
            if maxKey > len(longest):
                longest = lastDict[maxKey]
        return longest