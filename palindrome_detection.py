def return_reverse_string(input_string):

    stirng_length = len(input_string)
    newstring=''

    for i in range(stirng_length):
        newstring+=input_string[stirng_length-1]
        stirng_length-=1

    return newstring

original_string = 'abcd''''''''- dcba'
processed_original_string = original_string.replace(' ','').replace("'",'').replace("-",'')
print processed_original_string
reversed_string = return_reverse_string(processed_original_string)

if processed_original_string == reversed_string:
    print('True')