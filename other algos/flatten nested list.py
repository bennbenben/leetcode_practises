def flatten(input_list):
    # define recursive return case
    if input_list == []:
        return input_list

    # if first element is a list
    if type(input_list[0])==list:
        return flatten(input_list[0]) + flatten(input_list[1:])

    # recusive case - first element is not a list
    return input_list[:1] + flatten(input_list[1:])

s=[[1,2],[3,4]]
print(flatten(s))