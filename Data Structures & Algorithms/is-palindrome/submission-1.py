class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            # Keep incrementing or decrementing pointers if they aren't AlphaNumeric
            while not self.isAlphaNumeric(s[left]) and left < right:
                left += 1
            while not self.isAlphaNumeric(s[right]) and left < right:
                right -= 1
            
            # Convert to lowercase and compare the characters
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        # If the string comes out of while loop without returning False, then it is a Palindrome
        return True

    
    def isAlphaNumeric(self, char) -> bool:

        if (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')):
            return True
        else:
            return False