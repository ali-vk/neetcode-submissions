class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return Counter(s) == Counter(t)
        # if (len(s) != len(t)):
        #     return False
        # char = {chr(i): 0 for i in range(97, 123)}
        # for c1,c2 in zip(s,t):
        #     char[c1] += 1
        #     char[c2] -= 1
        # if (all(value == 0 for value in char.values())):
        #     return True
        # return False


        