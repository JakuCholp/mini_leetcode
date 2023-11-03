def replace_first_occurrence(input_string, search, replace):
    index = input_string.find(search)
    if index != -1:
        return input_string[:index] + replace + input_string[index + len(search):]
    else:
        return input_string
    


