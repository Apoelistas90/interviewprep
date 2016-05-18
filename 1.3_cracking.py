#Design an algorithm and write code to remove the duplicate characters in a string
#without using any additional buffer. NOTE: One or two additional variables are fine.
#An extra copy of the array is not.

def remove_dups_str(input_string):
    if input_string == '':
        return
    res=''
    chars_occ = {}
    for char in input_string:
        chars_occ[char]=1
        #print(chars_occ)



    return ''.join(chars_occ.keys())

print(remove_dups_str('asd'))
print(remove_dups_str('aaaa'))
print(remove_dups_str('aaaabbb'))
print(remove_dups_str('aaaabbbaa'))


print(remove_dups_str(''))