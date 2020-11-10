def quick_sort(my_list):
    length = len(my_list)
    if length <=1:
        return my_list
    else:
        pivot = my_list.pop()

    greater = []
    less = []

    for item in my_list:
        if item > pivot:
            greater.append(item)
        else:
            less.append(item)

    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1,3,4,5,6,2,19,15,20]))
