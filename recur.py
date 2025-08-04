import random 
def collate_strings(nested):
    strings = []
    if isinstance(nested, dict):
                    for value in nested.values():
                        strings.extend(collate_strings(value))
    elif isinstance(nested, list):
                        for item in nested:
                            strings.extend(collate_strings(item))
    elif isinstance(nested, str):
        strings.append(nested)
    return strings
def palindrome_check(unpass):
                   new_value = list(unpass)
                   return new_value == new_value.reverse()
def get_matrix(passed):
                       final_result = [ ]
                       for word in passed:
                           new_list = [ ]
                           chars = list(word)
                           window_size = max(2, len(chars) // 2)
                           random.shuffle(chars)
                           for _ in range(len(word) -window_size + 1):
                               choose = random.sample(chars, k=3)
                               new_list.append(choose)
                               final_result.append(new_list)
                   
data = {
    "a": ["racecar", {"x": ["noon", "apple"]}],
    "b": [["deed", "hello"], "world"],
    "c": {"inner": ["civic", ["radar", "python"]]}
}
next = collate_strings(data)
print(next)


next_list = [ num for num in next if palindrome_check(num) ]
print(next_list)

result = get_matrix(next)
print(result)

               
                   
                    
                    
                    
        