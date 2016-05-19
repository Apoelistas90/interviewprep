list = [ 12, 15 , 65 ,1, 23]

for i in range(len(list)-1):

    for j in range(len(list)-1) :

        if list[j]>list[j+1]:

            temp = list [j+1]
            list [j+1] = list[j]
            list [j] = temp


print(list)