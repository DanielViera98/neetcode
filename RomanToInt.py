#Thought Process: First thought was a switch statement. I knew it wouldn't be the most elegant or the best solution, but decided to write it out anyways.
#Simply iterate, check the current and next element, if they match a special combo, add to total and increment past. Otherwise increment and add based on i.

#Result: 11ms, beats 15% time, 65% memory.
class Solution:
    def romanToInt(self, s: str) -> int:
        dict double_values(IV = 4, IX= 9, XL= 40, XC= 90, CD= 400, CM= 900)

        total = 0
        i = 0
        while i < len(s):
            j = i+1
            if j < len(s):
                match s[i]+s[j]:
                    case "IV":
                        total += 4
                        i += 1
                    case "IX":
                        total += 9
                        i += 1
                    case "XL":
                        total += 40
                        i += 1
                    case "XC":
                        total += 90
                        i += 1
                    case "CD":
                        total += 400
                        i += 1
                    case "CM":
                        total += 900
                        i += 1
                    case _:
                        match s[i]:
                            case "I":
                                total += 1
                            case "V":
                                total += 5
                            case "X":
                                total += 10
                            case "L":
                                total += 50
                            case "C":
                                total += 100
                            case "D":
                                total += 500
                            case "M":
                                total += 1000
            else:
                match s[i]:
                            case "I":
                                total += 1
                            case "V":
                                total += 5
                            case "X":
                                total += 10
                            case "L":
                                total += 50
                            case "C":
                                total += 100
                            case "D":
                                total += 500
                            case "M":
                                total += 1000
            i += 1
        return total

#Thoughts: By using dictionaries to store the possible combinations, I can use the quick access time to my advantage. If s[i]+s[i+1] is found in double_values,
#use that value and increment twice. Otherwise, add the single_values and increment once.

#Result: 4ms, beats 65% time, 98% memory.
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        double_values = dict(IV = 4, IX= 9, XL= 40, XC= 90, CD= 400, CM= 900)
        single_values = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
        check_values = ['I', 'X', 'C']
        while i < len(s):
            if s[i] in check_values and len(s) > i+1:
                if s[i] + s[i+1] in double_values:
                    total += double_values[s[i]+s[i+1]]
                    i += 2
                else:
                    total += single_values[s[i]]
                    i += 1
            else:
                total += single_values[s[i]]
                i += 1
        return total

#This solution was taken from one of the submitted solutions, where instead of parsing they just replace all 2-character combinations with the elongated form,
#then calculate it with a translation dictionary. This problem seems subject to random results in hardware overall, as this sometimes performed better than the
#above and sometimes did not. 
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number