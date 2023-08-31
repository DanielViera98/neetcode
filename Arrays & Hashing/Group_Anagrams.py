#First Attempt:
'''
        x = {}
        n = len(strs)
        for i in range(n):
            x[i] = sorted(strs[i])
        # print(x)

        y = []
        for i in range(len(x)):
            if x[i] == -1:
                continue
            y.append([strs[i]])
            # print(i, x[i])
            for j in range(i+1,len(x)):
                # print(x[j])
                if (x[j] == -1):
                    continue
                if x[i] == x[j]:
                    y[len(y)-1].append(strs[j])
                    x[j] = -1
        # print(x)
        # print(y)
        return y 
'''
#Results: 6012 ms (5.2%), 18.6 mb (36.29%)

#Second Attempt:
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        results = []
        for string in strs:
            for y in results:
                if sorted(string) == sorted(y[0]):
                    y.append(string)
                    break
            else:
                results.append([string])

        #print(results)
        return results
'''
#Results: Time Limit Exceeded

#Solution:
'''
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
'''
#Explanation: Create a dictionary. For every provided word, sort it, and if there is a key equal to the sorted word in the dict, append the word to that entry. If there is no key, then it adds it to the dict.
#Finally, it returns the values of the dict.
