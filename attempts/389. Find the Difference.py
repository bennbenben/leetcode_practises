class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        utc_s_sum=utc_t_sum=0
        for i in s:
            utc_s_sum += ord(i)
        for i in t:
            utc_t_sum += ord(i)
        return chr(utc_t_sum-utc_s_sum)
