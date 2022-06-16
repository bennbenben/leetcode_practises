from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = list()
        count_s = Counter(s)
        
        # add the letters inside order to output list, multiplied by the # of times it appear
        for letter in order:
            output.append(count_s[letter] * letter)
        
        # add the letters in s but not in order to the output list
        for letter in s:
            if letter not in order:
                output.append(letter)
        
        # return combined string
        return "".join(output)