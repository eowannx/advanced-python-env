#Assignment 2 - task 6
def all_eq(lst):
    if not lst:
        return []
    
    max_length = 0
    for i in lst:
        if len(i) > max_length:
            max_length = len(i)
    
    result = []
    for i in lst:
        if len(i) < max_length:
            result.append(i + "_" * (max_length - len(i)))
        else:
            result.append(i)
    
    return result

string = ['addd', 'wewlw,', '2jd']
print(all_eq(string))