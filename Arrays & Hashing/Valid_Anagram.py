# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

s = "anagram"
t = "nagaram"

#First Try
'''
n = len(s)
m = len(t)
if (n != m):
    print(False)
    #return False
c = set()
for i in range(n):
    if s[i] in c:
        c.update(s[i][2]+1)
    else:
        c.add((s[i],1))
    print(c)

d = set()
for j in range(n):
    if t[j] in d:
        d.update(t[j][2]+1)
    else:
        d.add((t[j],1))
    print(d)
    
if c == d:
    return True
else:
    return False
'''
#Result: Fails on half the cases

#Actual Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
#This is the best solution, it does what I was trying to do but did not have the knowledge to do effectively