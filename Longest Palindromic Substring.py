class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        i = 0 
        while i < len(s):
            j = i
            while j < len(s):
                substring = s[i:j+1]     #slice the string in the range of i:j+1
                if substring == substring[::-1]:     # checking if palindromic or not
                    if len(substring) > len(res):    # check if the len of substring is greater then the len res
                        res = substring       # if substring len is greater the res will change to substring , if not res will remain same
                j+=1 
            i+=1
                    
        return res 
