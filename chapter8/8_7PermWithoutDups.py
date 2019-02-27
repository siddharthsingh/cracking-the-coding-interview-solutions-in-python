"""
This problem can be found on leetcode at the link
https://leetcode.com/problems/permutations/
"""

def create_perms(string,pos):
    """
    In this algorithm we recursively generate all the permutations. We build the anwer in bottom up approach.
    Pos tells us from which index we have to consider the string. When pos is the last index of string, we just return
    the char at that index. Then in the previous level we take this char and add the second last element at both sides
    of it. We build the answer in this manner adding the current char to every index of the result we got from pos+1.

    Total number of permutations of a string of length n is n!.

    Time complexity of this algorithm would be O(n!)

    Space complexity: Since we need to store all n! permutations, the space complexity would be O(n!)
    :param string:
    :param pos:
    :return:
    """
    # We are at the last index so just return the char
    if pos == len(string)-1:
        return [[string[pos]]]
    answers_from_next_position = create_perms(string,pos+1)
    # used to generate the answer of current index
    current_pos_answer = []
    # for every permutation we got from next index, insert the current char at every index of every permutation
    for answer in answers_from_next_position :
        i = len(answer)
        while i>=0:
            # lists are mutable, we need to copy the current permutation, then insert the char at index and store it
            # in our final answer
            copy_of_answer = answer[:]
            copy_of_answer.insert(i,string[pos])
            current_pos_answer.append(copy_of_answer)
            i = i-1
    return current_pos_answer

print(create_perms(list("abc"),0))
