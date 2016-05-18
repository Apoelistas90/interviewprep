my_list = [3, 4, 6]
alices_list = [1, 5, 8]

def sort_merge_lists2(my_list,alices_list):
    merged_list=[]


    total_len = len(my_list)+len(alices_list)
    merged_list = [None] * total_len



    myindex = 0
    alicesindex = 0
    mergedindex = 0

    while mergedindex < total_len:
        print merged_list

        ismylistexhausted = myindex >=len(my_list)
        isaliceslistexhausted = alicesindex>=len(alices_list)

        if not isaliceslistexhausted and ( ismylistexhausted or my_list[myindex] > alices_list[alicesindex]):
            merged_list[mergedindex] = alices_list[alicesindex]
            alicesindex+=1

        else:
            merged_list[mergedindex] = my_list[myindex]
            myindex+=1

        mergedindex+=1

    return merged_list



def sort_merge_lists(my_list,alices_list):
    merged_list=[]
    total_len = len(my_list)+len(alices_list)
    while len(merged_list) < total_len:
        print merged_list

        if len(my_list) == 0 and len(alices_list) == 0:
            break

        if len(my_list) == 0:
            merged_list.append(alices_list[0])
            alices_list.pop(0)
            continue
        if len(alices_list) == 0:
            merged_list.append(my_list[0])
            my_list.pop(0)
            continue

        if my_list[0]>alices_list[0]:
            merged_list.append(alices_list[0])
            alices_list.pop(0)
        elif alices_list[0]>my_list[0]:
            merged_list.append(my_list[0])
            my_list.pop(0)
    return merged_list





my_list = [3,5,6]
alices_list = [1, 5, 8]

print sort_merge_lists2(my_list,alices_list)



def merge_lists(my_list, alices_list):

    # set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:

        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)

        # case: next comes from my list
        # my list must not be exhausted, and EITHER:
        # 1) alice's list IS exhausted, or
        # 2) the current element in my list is less
        #    than the current element in alice's list
        if not is_my_list_exhausted and (is_alices_list_exhausted or \
                (my_list[current_index_mine] < alices_list[current_index_alices])):

            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1

        # case: next comes from alice's list
        else:
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list

print merge_lists(my_list,alices_list)
