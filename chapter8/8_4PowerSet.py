class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        self.ans = []
        self.store = {}
        a = self.helper(nums, len(nums))
        # a.add(())
        ans = [list(x) for x in a]
        ans.append([])

        return ans

    #     def helper2(self,nums,pos,temp):
    #         if pos == len(nums)-1:
    #             self.ans.append(temp)

    #         for i in range(pos,len(nums)):
    #             num = nums[i]
    #             self.ans.append(num)
    #             temp.append(num)
    #             a = helper2(nums,pos+1,temp)
    #             temp.pop()

    def helper(self, nums, l):
        if l in self.store:
            return self.store[l]
        ans = set()
        if l == 1:
            for num in nums:
                ans.add(tuple([num]))
            return ans
        a = self.helper(nums, l - 1)
        for num in nums:
            for aa in a:
                if num not in aa and len(aa) == l - 1:
                    ans.add(tuple(sorted([num] + list(aa))))
        ans = ans.union(a)
        self.store[l] = ans
        return ans

