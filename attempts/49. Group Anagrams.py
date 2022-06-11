class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        output = list()
        
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagram_map.keys():
                anagram_map[sorted_string].append(string)
            else:
                anagram_map[sorted_string] = [string]
        
        for val in anagram_map.values():
            output.append(val)
        
        return output