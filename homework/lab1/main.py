########## 1 ##########

# insert numbers from console
a = int(input("1. Enter first number "))
b = int(input("Enter second number "))
def gcd(a, b):
    while b:
        a, b = b, a % b #go through the loop until b = 0 checking if a is divisible by b each time
    return a

result = 0
for num in [a, b]:
    result = gcd(result, num) #recursive function to repeat the gcd function until the list is empty

print("GCD:", result)

########## 2 ##########

#input reads things from console
string = input("2. Enter a string ")

#add all vowels to a string
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

########## 3 ##########

# Read strings from the console
string1 = input("3. Enter the first string ")
string2 = input("Enter the second string ")

# Count occurrences
count = string2.count(string1)
print("Number of occurrences:", count)

########## 4 ##########

# Read UpperCamelCase string from the console
upper_camel_case = input("4. Enter UpperCamelCase string: ")

# Convert to lowercase_with_underscores
def camel_case_to_requested(input_string):
    output_string = [input_string[0].lower()] #first letter is always lowercase
    for char in input_string[1:]: #loop through the rest of the string
        if char.isupper(): #if the character is uppercase, add an underscore and the lowercase version of the character
            output_string.extend(['_', char.lower()]) #extend adds multiple elements to a list
        else:
            output_string.append(char)#if the character is lowercase, just add it to the list, append adds one element to a list
    return ''.join(output_string) #join the list into one string

requested_case = camel_case_to_requested(upper_camel_case)
print("Lowercase with underscores:", requested_case)

########## 5 ##########
def spiral_order(matrix):
    result = []
    #so long as there are still elements in the matrix we iterate through it and pop the first row
    while matrix:
        result += matrix.pop(0) #pop the first row and add it to the result
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop()) #pop the last element of each row and add it to the result now
        if matrix:
            result += matrix.pop()[::-1] #pop the last row and add it to the result in reverse order
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0)) #pop the first element of each row and add it to the result now in reverse order
    return ''.join(result) #join the list into one string (opposite of split)

# ex
matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]
#create a copy of the matrix
matrix_copy = matrix.copy()
print("5. We went from this: \n", matrix_copy, "\n to this: \n", spiral_order(matrix))  # output first_python_lab <3 cute


########## 6 ##########

number = int(input("6. Enter a number "))
def is_palindrome(number):
    return str(number) == str(number)[::-1] # [::-1] reverses the string or whatever else you put in the brackets

if is_palindrome(number):
    print("This number is palindrome")
else:
    print("This number is not palindrome")

########## 7 ##########

text = input("7. Enter a string ")
def extract_number(text):
    num_str = ""
    for char in text:
        if char.isdigit():  # isdigit() checks if the character is a digit
            num_str += char
        elif num_str:
            break
    if num_str:
        return int(num_str)
    return None

#ex
print(extract_number("An apple is 123 USD"))  # output 123
print(extract_number("abc123abc"))  # output 123
print ("The extracted number is ", extract_number(text))


########## 8 ##########

number = int(input("8. Enter a number "))
def count_ones(number):
    count = 0
    while number:
        count += number & 1 # & is a bitwise operator that compares two numbers bit by bit and returns 1 if both bits are 1
        number >>= 1 # >> is a bitwise operator that shifts the bits of the number to the right by the number of bits specified after it
    return count

print("Binary representation of the number is ", bin(number))
print("Number of ones:", count_ones(number))

########## 9 ##########

text = input("9. Enter a string ")
def most_common_letter(text):
    letter_counts = {}
    max_letter = ''
    max_count = 0

    for char in text:
        if char.isalpha():  # isalpha() checks if the character is a letter
            char_lower = char.lower() #convert the character to lowercase
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1 #get the value of the key char_lower, if it doesn't exist, return 0 and add 1 to it
            if letter_counts[char_lower] > max_count: #if the value of the key char_lower is greater than the current max_count, set the max_count to the value of the key char_lower and set the max_letter to char_lower
                max_count = letter_counts[char_lower]
                max_letter = char_lower

    return max_letter, max_count


#example
print(most_common_letter("an apple is not a tomato"))  #output ('a', 4)
print(most_common_letter(text))

########## 10 ##########

text = input("10. Enter a string ")
def count_words(text):
    words = text.split() #split the string into a list of words..use instead of two inputs?
    return len(words) #return the length of the list of words

print("Number of words ", count_words(text))
