def add_sum(nums,target):
    for i in range(len(nums)):
        for x in range(len(nums)):
            if nums[x] + nums[i] == target and x != i:
                print(f"x {x} i {i} win")
                print(f"sum = {nums[x] + nums[i]}")
                return [i,x]
            else:
                print(f"x {x} i {i} no")

print(add_sum([2,7,11,15], 9))