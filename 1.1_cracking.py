#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

def has_unique_chars(input_string):
    seen_chars = []
    for char in input_string:
        #print char
        if char in seen_chars:
            return False
        else:
            seen_chars.append(char)

    return True

print(has_unique_chars('avac'))