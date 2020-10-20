
#first implementation of selection sort
#selection sort max -> min
def selection_sort(list):
    curr_index = 0
    curr_max = 0
    while curr_index <= len(list) -1:
        for index in range(curr_index,len(list)):
            value = list[index]
            if curr_max < list[index]:
                curr_max, list[index] = list[index], curr_max
        list[curr_index] = curr_max
        curr_index +=1
        curr_max = 0
    print(list)
   
#second implementation of selection sort
# min -> max
def selection_2(list):

    for index in range(0,len(list)-1):
        maxNum = list[index]
        for index2 in range(index+1, len(list)):
            if list[index2] <= maxNum:
                maxNum, list[index2]  = list[index2], maxNum
        list[index] = maxNum
    print(list)


print("Selection sort 1: ")
selection_sort([6,2,2,3,4,1])
print("Selection Sort 2: ")
selection_2([6,2,2,3,4,10])
        