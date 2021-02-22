def add_sum(nums,target):
    for i in range(len(nums)):
        for x in range(len(nums)):
            if nums[x] + nums[i] == target and x != i:
                return [i,x]


def add_sum_faster(nums_array,target_value):

    nums_dict = {}

    for i in range(len(nums_array)):
        if target_value - nums_array[i] in nums_dict:
            return([nums_dict[target_value-nums_array[i]], i])
        else:
            nums_dict[nums_array[i]] = i


print(add_sum([2,7,11,15], 9))
print(add_sum_faster([2,7,11,15], 9))