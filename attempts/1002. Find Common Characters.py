from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_counter = Counter(words[0])
        for i in range(1, len(words)):
            curr_counter = Counter(words[i])
            min_counter = min_counter & curr_counter
        return min_counter.elements()