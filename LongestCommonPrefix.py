#Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

#First thought, check each element against the element of the min length string, return when they dont match. Obvious problem in time, as it is O(mn),
#Where m is length of minStr, and n is the number of strings in strs. 

#Results: 4ms, beats 11% time, 78% memory
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minStr = min(strs)
        result = ""
        for i in range(len(minStr)):
            for j in strs:
                if j[i] != minStr[i]:
                    return result
            result += minStr[i]
        return result

#Result: 0ms, beats 100% time, 30% mem
class Solution2:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minStr = (min(strs, key=len))                           #ensure that the only comparison is len
        strs.remove(minStr)                                     #remove minstr from strs so that it is not compared to itself.
        result = ""
        for i in range(len(minStr)):
            for j in strs:
                if j[i] != minStr[i]:
                    return result
            result += minStr[i]
        return result
    
#Thoughts: change how I compare strings to compact code. Used zip to get a list of the strings based on the shortest, and set to check if all elements are the same.

#Result: 0ms, beats 100% time, 95% space
class Solution3:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        for i in zip(*strs):
            if len(set(i)) > 1:
                return result
            result += i[0]
        return result
    
r = Solution3()
print(r.longestCommonPrefix(["flower","flow","flight"]))

