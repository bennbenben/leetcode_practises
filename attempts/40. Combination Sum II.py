class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = list()
        candidates.sort()
        
        def combinations(curr, target, pos):
            if target == 0:
                output.append(curr.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                combinations(curr, target-candidates[i], i+1)
                curr.pop()
                prev = candidates[i]
        
        combinations([],target,0)
        # print(output)
        return output