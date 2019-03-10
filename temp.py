def find_missing(nums):
    # this will be 100 in our case
    len_of_nums = len(nums)+1
    ideal_sum = (len_of_nums*(len_of_nums+1))/2
    actual_sum = sum(nums)
    return int(ideal_sum - actual_sum)

print(find_missing([3,4,5,6,7,8,2,9,10] ))