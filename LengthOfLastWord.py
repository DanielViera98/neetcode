#Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal consisting of non-space characters only.

#Thoughts: iterate from back of string, if a space is encountered, return length (unless length is 0, since a word is not encountered). Else, decrement i
#and increase length

#Result: 0ms, beats 100% time, 60% mem
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        length = 0
        while i >= 0:
            if s[i] == " ":
                if length != 0:
                    return length
                i -= 1
            else:
                i -= 1
                length += 1
        return length
    

#Posted Solution

#Thoughts: same time, worse memory. Shorter, uses functions of string. Strip removes whitespaces from front and end, split returns a substring list.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
        return len(words[-1])