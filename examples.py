temp_list = [1,2,3,4,5]

def get_highest_product(alist):
    highest_2 = [alist[0],alist[1]]
    highest = max(alist)
    for n in range(len(alist)):
        if n == 0 or n == 1:
            continue;
        if alist[n]>highest_2[0] and alist[n] <> highest:
            highest_2[0] = alist[n]



        highest_product_of_3 = alist[n] * highest_2[0] * highest_2[1]


        #print( str(n) + ' ' + str(highest_product_of_2))


    return highest_product_of_3

#print(get_highest_product(temp_list))


########

