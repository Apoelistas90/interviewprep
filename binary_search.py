#sample_list = [14,2,69,5,22,34,51,6,3,23,24,100,35]
sample_list = [1,3,7,9,15,18]

size = len(sample_list)

value_to_be_found = 3

sorted_sample_list = sorted(sample_list)
print(sorted_sample_list)


startindex = 0
endindex = len(sorted_sample_list) -1

runs = 0

while(True):
    print('')

    print('RUN #' + str(runs))
    middleIndex = (endindex+startindex)/2
    print('Startindex is ' + str(startindex))
    print('Endindex is ' + str(endindex))
    print('Middleindex is ' + str(middleIndex))


    if value_to_be_found>sorted_sample_list[middleIndex]:
        startindex=middleIndex+1
    elif value_to_be_found<sorted_sample_list[middleIndex]:
        endindex=middleIndex-1
    else:
        print('')
        print('Result is: '+str(middleIndex) +  ' index and value: ' + str(sorted_sample_list[middleIndex]))
        break
    runs+=1



