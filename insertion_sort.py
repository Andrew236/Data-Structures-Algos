# here is my implementation of an iterative insertion sort algorithim


def insertion(list):
    for index in range(1, len(list)):
        x = index - 1
        while x >= 0 and list[x] > list[index]:
            list[x], list[index] = list[index], list[x]
            x -= 1
            index -= 1
    print(list)


print("Insertion Sort: ")
insertion([10, 2, 3, 5, 2, 1])