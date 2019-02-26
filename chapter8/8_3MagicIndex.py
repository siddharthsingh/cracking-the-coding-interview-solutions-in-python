# Part 1 : A magic index in an array A[0..n-1] is defined to be an index such that A[i] = i. Given a sorted array of
# distinct integers, write a method to find a magic index, if one exists, in array A.
# No duplicates in the array

def magic_index(arr):
    """
    Since there are no duplicates we can do a binary search on the array to find the magic index.
    find the middle index, if the integer at the middle index is greater than the middle index search towards the left
    side of the arrray as every element on the right of the middle index will be greater than the element.
    :param arr:
    :return:
    """
    if not arr:
        return
    s = 0
    e = len(arr)-1
    while s <= e:
        mid = (s+e)//2
        print(arr[mid])
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            e = mid-1
        else:
            s = mid+1
    return -1

# part 2 : The values in the array are not distinct

def magic_index_part2(arr,start, end):
    """
    The method in part one will fail here because the magic index can be on either side of the mid index
    For example take a look at the following example:
    arr =   [-3,-2, 2, 2, 3, 6, 6]
    index = [ 0, 1, 2, 3, 4, 5, 6]
    Here the middle element would be at index 3 but as you can see the magic index is on both sides of the mid index.
    But if we look at the arr and index closely, we can see a patern.
    Look at index 3, the value there is 2, so the magic index can be on the left had side at position 0 to min(mid index
    , arr[mid_index])(it cant be any value between min(mid index, arr[mid_index])) to mid index because any thing on
    that range would have value equal to
    and on the right hand side at position max(mid index,arr[mid_index]) to end
    :param arr:
    :return:
    """
    # print(start,end)
    if start>end:return -1
    mid = (start+end)//2
    if mid == arr[mid]:
        return mid
    left = magic_index_part2(arr,start,min(mid-1,arr[mid]))
    # if it is on the left side, the returned value would not be -1, it would be the magic index
    if left != -1:
        return left
    right = magic_index_part2(arr,max(mid+1,arr[mid]),end)
    return right

arr = [-3,-2,-1,2,4,6,8]
arr2 = [-3,-2,-1,2,3,6,6]
arr2 = [-3,-2,2,20,21,22,23]
arr3 = [-3,-2,1,1,1,2,4,6,8]
arr4 = [0,2,3,4,5,6,40,60,80]
arr5 = [1,2,3,4,5,6]
# print(magic_index(arr))
print(magic_index_part2(arr2,0,len(arr2)-1))
# print(magic_index(arr3))
# print(magic_index(arr4))
# print(magic_index(arr5))