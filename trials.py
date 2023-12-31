"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    result = []

    for i, item in enumerate(items):
        if i % 2 != 0:
            result.append(item[i])
    
    return result



def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):
    nums = []

    for i in range(start, stop):
        nums.append(i)

    return nums



def censor_vowels(word):
    chars = []

    for letter in word:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            chars.append('*')
        else:
            chars.append(letter)
    
    return ''.join(chars)



def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(word[0].upper())
        camel_case.append(word[1:])
    
    return ''.join(camel_case)



def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result)-1]:
            result.append(char)
    
    return ''.join(result)
print(truncate('aaaabbbbcccca'))

def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
