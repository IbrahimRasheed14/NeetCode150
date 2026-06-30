class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = set(nums)
        longest = 0

        for x in number:
            if (x - 1) not in number:
                current = x
                length = 1

                while(current + 1)in number:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
                

        
        

        