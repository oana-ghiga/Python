#####1#####
#similar to 3 from h2 but with sets
def operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    diff_a = set(a) - set(b)
    diff_b = set(b) - set(a)
    return [intersection, union, diff_a, diff_b]

a = [1, 3, 5 ,6, 7]
b = [1, 2, 3, 4 , 5]
result = operations(a, b)
print("1. intersection, union, a - b, b - a:", result)


#####2#####
#sort the text by the number of occurrences of each character
def char_frequency(text):
    dictionary = {}
    for char in text:
        dictionary[char] = dictionary.get(char, 0) + 1 #if the character is not in the dictionary add it with a count of 1, otherwise we increment the count by 1
    return dictionary

text = "Ana has apples."
result = char_frequency(text)
print("2. the sorted text will be:", result)


#####3#####
#compare dictionaries without ==
def compare_dictionaries(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):  # get the keys from both dictionaries
        keys1 = set(dict1.keys()) # use set to make sure that the keys are unique
        keys2 = set(dict2.keys()) # this reminds me of SI for some reason
        if keys1 != keys2: # if the keys are not the same, dictionaries are different
            return False
        for key in keys1:  #go through keys and compare values recursively
            if not compare_dictionaries(dict1[key], dict2[key]):
                return False
        return True
    else:
        return dict1 == dict2 # if the values are not dictionaries, compare them directly


dict1 = {
    'a': 1,
    'b': [1, 2, 3],
    'c': {
        'd': 4,
        'e': {
            'f': 5
        }
    }
}
dict2 = {
    'a': 1,
    'b': [1, 2, 3],
    'c': {
        'd': 4,
        'e': {
            'f': 5
        }
    }
}
dict3 = {
    'a': 1,
    'b': [1, 2, 3],
    'c': {
        'd': 4,
        'e': {
            'f': 6  # different value
        }
    }
}

print("3. first comparation", compare_dictionaries(dict1, dict2))  # Output: True
print("second comparation", compare_dictionaries(dict1, dict3))  # Output: False

#####4#####
#build an xml element... had to search up XML
def build_xml_element(tag, content, **kwargs): #kwargs is a dictionary of attributes and their values -> ngl stackoverflow helped me with this one
    attributes = ' '.join([f'{key}="{value}"' for key, value in kwargs.items()]) #using list comprehension to get the attributes and their values
    return f'<{tag} {attributes}>{content}</{tag}>'

# Example usage:
element = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print("4.your brand new xml", element)

#####5#####
# validate a dictionary based on a set of rules
def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules: #unpacking the rules tuple aka key, prefix, middle, suffix = rules
        if key in dictionary:
            value = dictionary[key] #get the value of the key
            if not value.startswith(prefix) or not value.endswith(suffix): #check if the value starts with the prefix and ends with the suffix
                return False
            middle_index = value.find(middle) #get the index of the middle string
            if middle_index == -1 or middle_index == 0 or middle_index == len(value) - len(middle): #if the middle string is not in the value or it's at the start or end of the value, then the dictionary is not valid
                return False
        else:
            return False
    return True

rules = [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")]
dictionary = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print("5. and the result will beeeeee:", validate_dict(rules, dictionary))


#####6#####
#count the number of unique and duplicate elements in a list
def count_elements(lst):
    unique_set = set()
    duplicates_set = set()

    for item in lst:
        if item in unique_set:
            duplicates_set.add(item)
            unique_set.discard(item)
        else:
            unique_set.add(item)

    unique_count = len(unique_set) - 1
    duplicate_count = len(duplicates_set)

    return unique_count, duplicate_count

lst = [1, 2, 2, 3, 4, 4, 4, 5 ,6 , 9, 9]
result = count_elements(lst)
print("6. first element is the number of uniques and the second is duplicates", result)


#####7#####

def set_operations(*sets):
    operations = {}
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            key = f"{sets[i]} | {sets[j]}" #using f-strings to get the operations
            operations[key] = sets[i] | sets[j] #using | to get the union
            key = f"{sets[i]} & {sets[j]}" #using & to get the intersection
            operations[key] = sets[i] & sets[j] #using - to get the difference
            key = f"{sets[i]} - {sets[j]}" #using - to get the difference
            operations[key] = sets[i] - sets[j]
            key = f"{sets[j]} - {sets[i]}"
            operations[key] = sets[j] - sets[i]
    return operations

set1 = {1, 2}
set2 = {2, 3}
result = set_operations(set1, set2)
print("7. Results are: ", result)


#####8#####

def loop(mapping):
    seen = set()
    result = []
    current_key = "start"
    while current_key not in seen: #while the current key is not in the seen set we add it to the result and get the next key
        seen.add(current_key) #add the current key to the seen set
        result.append(current_key) #add the current key to the result
        current_key = mapping.get(current_key) #get the next key
    return result

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping) #go in a loop until we get to a key that we've already seen
print("8. Result:", result)

#####9#####

def my_function(*args, **kwargs): #args is a tuple of arguments, kwargs is a dictionary of keyword arguments
    return sum(arg in kwargs.values() for arg in args) #check if the argument is in the values of the kwargs dictionary and sum the results

result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print("9. Result:", result)
