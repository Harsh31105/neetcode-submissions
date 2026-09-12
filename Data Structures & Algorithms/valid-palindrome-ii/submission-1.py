class Solution:
    def validPalindrome(self, s: str) -> bool:
        if (len(s) == 0 or len(s) == 1):
            return True
        
        if s[0] == s[-1]:
            return self.validPalindrome(s[1:-1])
        else:
            skip_first = s[0:-1]
            skip_last = s[1:]

            return self.palindrome(skip_first) or self.palindrome(skip_last)

    def palindrome(self, s: str) -> bool:
        text = s
        reverse = text[::-1]
        return text == reverse