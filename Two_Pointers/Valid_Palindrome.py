class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        for i in s:
            if i.isalnum() is False:
                s = s.replace(i, "")
        t = slice(0, int(len(s)/2))
        z = zip(reversed(s), s[t])

        for i in z:
            if i[0] != i[1]:
                return False

        return True
