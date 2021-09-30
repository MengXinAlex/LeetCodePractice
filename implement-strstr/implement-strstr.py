class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
    
        return -1


                
        # brute force timeout
        
#         for i in range(len(haystack)-len(needle)+1):
#             found = True
#             length = 0
#             for j in range(len(needle)):
#                 # print(haystack[i+length], needle[j])
#                 if haystack[i+length] != needle[j]:
#                     found = False
#                     break
#                 else:
#                     length+=1 
#             if found: 
#                 return i
#         return -1
