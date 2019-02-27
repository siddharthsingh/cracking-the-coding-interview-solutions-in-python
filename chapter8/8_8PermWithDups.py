from collections import defaultdict

"""
This problem can be found on leetcode at the link
https://leetcode.com/problems/permutations-ii/
"""

def create_perms(string, pos):
    """
    Time and space complexity of this algorithm is O(n!)
    This is a simple/same algorith we used in the previous question 8.7. The only difference is that we are checking to
    make sure we dont add a permutation that is already there in the result.
    Although this works and we can't do better in terms of worst case time complexity, we can improve the time a lot
    for average case by using a different algorithm.

    The new algorithm is the function faster_create_perms_with_dups

    :param string:
    :param pos:
    :return:
    """
    if pos == len(string) - 1:
        return [[string[pos]]]
    answers_from_next_position = create_perms(string, pos + 1)
    current_pos_answer = []
    for answer in answers_from_next_position:
        i = len(answer)
        while i >= 0:
            copy_of_answer = answer[:]
            copy_of_answer.insert(i, string[pos])
            if copy_of_answer not in current_pos_answer:
                current_pos_answer.append(copy_of_answer)
            i = i - 1
    return current_pos_answer
@staticmethod
def helper(char_count,generated,res):

    if not char_count:
        res.append(generated[:])
    # creating a copy of the items in the dictionary, this is requires because we are modifying the items of the
    # dictionary inside the for loop. So if we loop over the actual dictionary it would have the side effect because of
    # the line where we increment the counter of char, the number of times the for loop will get executed will be more
    # than the number of keys.
    # If the above point is not clear try looping over the actual dictionary and put break points and step through the
    # code line by line you would see the side effect.
    items = list(char_count.items())
    for char, count in items:
        char_count[char] -=1
        generated.append(char)
        if count == 1:
            del char_count[char]
        helper(char_count,generated,res)
        generated.pop()
        char_count[char]+=1



def faster_create_perms_with_dups(string):
    """
    This algorithm also has the worst case time complexity of O(n!) but it would perform much better in average case.
    Ths space complexity remains the same
    :param string:
    :return:
    """
    char_count = defaultdict(lambda :0)
    for char in string:
        char_count[char] += 1
    result = []
    helper(char_count,[],result)
    print(len(result))
    return result



print(faster_create_perms_with_dups("aabc"))
