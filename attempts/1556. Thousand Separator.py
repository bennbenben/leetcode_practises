class Solution:
    def thousandSeparator(self, n: int) -> str:
        """
        1. find out how many dots are needed
        2. iterate backwards to include the dots
        """
        # define variables
        n_str = str(n) # work in strings
        n_copy = n # n is an int(). primitive data types do not need copy.deepcopy() method
        track_thousands = 0
        output = str()
        counter = 0
        
        # find out how many dots are needed
        while n_copy//1000 != 0:
            n_copy = n_copy%1000
            track_thousands += 1
        
        # iterate backwards to include the dots
        for i in range(len(n_str)-1, -1, -1):
            output += n_str[i]
            counter += 1
            if counter % 3 == 0:
                output += "."
                counter = 0
            
        # reformat output for final answer
        output = output[::-1]
        if output[0] == ".":
            return output[1:]
        else:
            return output