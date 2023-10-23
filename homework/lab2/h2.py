#h2  lists


######1#####
#first n numbers in the Fibonacci
def fibonacci(n):
    fib_list = [] #list for numbers
    a, b = 0, 1 #we gotta start somewhere so 0, 1
    for _ in range(n):
        fib_list.append(a) #add a to the list append adds one element to the end of the list, extend adds multiple elements
        a, b = b, a + b #a is now b and b is now a + b -> cool thing with the double assignment
    return fib_list
print("1. Fibonacci:", fibonacci(10))


#####2#####
#prime numbers in a list
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1): #we only need to check until the square root of n, because if n is divisible by a number greater than its square root, then it is also divisible by a number smaller than its square root
        if n % i == 0:
            return False
    return True
def find_prime(numbers): #list comprehension
    return [n for n in numbers if prime(n)] #if prime(n) is true, then n is added to the list

print("2. Prime numbers:", find_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))


#####3#####
#operations with lists
def operations(a, b):
    intersection = list(set(a) & set(b)) #using list in front of set to convert the set to a list
    union = list(set(a) | set(b))
    diff_a = list(set(a) - set(b))
    diff_b = list(set(b) - set(a))
    return intersection, union, diff_a, diff_b

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print("3. intersection, union, a - b, b - a:", operations(a, b))

#####4#####
#song composition
def compose(notes, moves, start_position): #notes is a list of strings, moves is a list of integers, start_position is an integer
    song = []
    current_position = start_position #need to keep track of the current position
    song.append(notes[current_position])  #add the first note to the song -> without this it won't print the mi
    for move in moves:
        current_position = (current_position + move) % len(notes) #use modulo to make sure that the current position is always between 0 and len(notes) - 1
        song.append(notes[current_position])
    return song

notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2
print("4. song:", compose(notes, moves, start_position))


#####5#####
#replace elements below the main diagonal with 0

def replace(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j < i:  # Only set elements below the main diagonal to 0
                matrix[i][j] = 0
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("5. matrix with everything below the main diagonal 0:", replace(matrix))



#####6#####
#weird find the items in the list thingy
def x_in_lists(x, *lists):
    all_items = [item for sublist in lists for item in sublist]
    item_counts = {}  # use a dictionary to store item counts -> ai homework showed why dictionaries are better than lists
    for item in all_items:
        item_counts[item] = item_counts.get(item, 0) + 1  # if the item is not in the dictionary add it with a count of 1, otherwise we increment the count by 1
    return [item for item, count in item_counts.items() if count == x]

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x = 1
print(f"6. items that appear {x} times: {x_in_lists(x, list1, list2, list3, list4)}")


#####7#####
#palindrome- how many and the greatest
def is_palindrome(num):
    return str(num) == str(num)[::-1] #use slicing to reverse the string

def palindrome(numbers):
    palindrome_numbers = [num for num in numbers if is_palindrome(num)] #list comprehension to get all the palindromes
    greatest_palindrome = max(palindrome_numbers) if palindrome_numbers else None #if palindrome_numbers is empty, then the greatest palindrome is None
    return len(palindrome_numbers), greatest_palindrome #returning a tuple

numbers = [121, 1331, 123, 454]
palindrome_count, greatest_palindrome = palindrome(numbers)
print(f"7.this many palindromes: {palindrome_count} and the greatest of them all is: {greatest_palindrome}")


#####8#####
#ascii lists and division by x
def ascii_lists(x=1, strings=None, flag=True): #x is the divisor, strings is a list of strings, flag is a boolean that tells us if we want the chars that are divisible by x or not
    if strings is None:
        strings = []
    result = []
    for string in strings:
        ascii_chars = [char for char in string if ord(char) % x == 0] \
            if flag else [char for char in string if ord(char) % x != 0] #using ord to get the ascii value of the char
        result.append(ascii_chars)
    return result

x = 2
strings = ["test", "hello", "lab002"]
flag = False
print(f"8. Generated ASCII lists: {ascii_lists(x, strings, flag)}")


#####9#####
#bad seats in a stadium
def peopleWhoCantSee(matrix):
    bad_seats = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(1, rows):
        for j in range(cols):
            for k in range(i): #gotta use 3 fors to check if the seat is lower than the seats in the rows above it
                if matrix[i][j] <= matrix[k][j]: #if the seat is lower than the seats in the rows above it, then it's a bad seat
                    bad_seats.append((i, j))
                    break
    return bad_seats


stadium = [[1, 2, 3, 2, 1, 1],
           [2, 4, 4, 3, 7, 2],
           [5, 5, 2, 5, 6, 4],
           [6, 6, 7, 6, 7, 5]]
print("9. bad seats:", peopleWhoCantSee(stadium))


#####10#####
#rearranging lists
def rearrange(*lists):
    max_length = max([len(lst) for lst in lists]) #getting the max length of the lists so we know how many elements to take from each list
    new_lists = []
    for i in range(max_length): #using list comprehension to create a tuple of the elements from each list
        combined_tuple = tuple(lst[i] if i < len(lst) else None for lst in lists) #if the list is shorter than max_length, then we add None to the tuple
        new_lists.append(combined_tuple) #adding the tuple to the list
    return new_lists

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
print("10.The rearranged lists are:", rearrange(list1, list2, list3))


#####11#####
#sorting tuples by the third character
def sort_tuples_by_third_character(words): #words is a list of tuples of strings
    return sorted(words, key=lambda x: x[1][2]) #using lambda to get the third character of the second element of the tuple and then sorting the list of tuples by that character
#lambda is an anonymous function, it's used when you need a function only once and you don't want to define it separately, key is a parameter of the sorted function, it's used to specify a function that is used to extract a comparison key from each list element

word_tuples = [('abc', 'bcd'), ('abc', 'zza')]
print("11.the new tuples:", sort_tuples_by_third_character(word_tuples))

#####12#####
#rhyming game
def rhyme(words):
    rhyme_dict = {} #dictionary to store the words grouped by rhyme key...after ai it's better to use dictionaries instead of lists
    for word in words:
        rhyme_key = word[-2:] #the rhyme key is the last 2 characters of the word
        if rhyme_key in rhyme_dict: #if the rhyme key is already in the dictionary, then we add the word to the list of words that rhyme
            rhyme_dict[rhyme_key].append(word) #we use append because we're adding to a list
        else:
            rhyme_dict[rhyme_key] = [word] #if the rhyme key is not in the dictionary, then we create a new list with the word
    grouped_words = list(rhyme_dict.values()) #we use list to convert the values of the dictionary to a list of lists
    return grouped_words

words = ['ana', 'banana', 'carte', 'arme', 'parte']
print("12.words grouped by rhyme:", rhyme(words))