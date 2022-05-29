from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        strs = "\n".join(source) + "\n"
        i=0
        output_str=str()
        while i < len(strs):
            if strs[i] == "/" and strs[i+1] == "/" and i+1 < len(strs):
                next_i = strs.find("\n",i+2)
                i = next_i
            if strs[i] == "/" and strs[i+1] == "*" and i+1 < len(strs):
                next_i = strs.find("*/",i+2)
                i = next_i+2
            else:
                output_str += strs[i]
                i+=1
        
        output_prog = output_str.split('\n')
        
        i=0
        while i < len(output_prog):
        	if output_prog[i] == "":
        		output_prog.pop(i)
        	else:
        		i+=1
        return output_prog
        
s = Solution()
print(s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
