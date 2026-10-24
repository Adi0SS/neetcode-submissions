class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for character in s:
            if character not in count_s:
                count_s[character] = 1
            else:
                count_s[character] +=1
        for character in t:
            if character not in count_t:
                count_t[character] = 1
            else:
                count_t[character] += 1

        for key,value in count_s.items():
            if key not in count_t:
                return False
            if count_t[key] != value:
                return False

        return True        



        