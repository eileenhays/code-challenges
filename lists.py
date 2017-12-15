# Determine the highest profit that can be made in a day from one purchase and one sale that day. Given a list of stock prices where indices is minute(s) past open trading. 

#   Example: if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500

def highest_profit(lst):
  
  hp = 0
  i = 0 
  
  while i < len(lst) - 1:
    j = i + 1
    right = lst[j]
    left = lst[i]

    if right > left: 
      curr_delta = right - left
      if curr_delta > hp: 
        hp = curr_delta
        j += 1
   
    i += 1
  
  return hp

## Tests ##    
lst = [10, 7, 5, 6, 12, 2]
high_profit(lst) == 7


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# Example:
# input: nums = [2, 7, 11, 15], target = 9
# output: [0, 1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """      
    # O(n^2) solution    
#         for idx1, num1 in enumerate(nums):
#             for idx2, num2 in enumerate(nums):
#                 if (num1 + num2) == target and idx1 != idx2:
#                     return [idx1, idx2]
        
#         return None

# Runtime: O(n)
        complement = {}
        
        for idx, num in enumerate(nums):            
            if num in complement:
                return [complement[num], idx]
            else: 
                complement[target - num] = idx

## Tests ##    
lst = [2, 7, 11, 15]
target = 9
test1 = Solution()
test1.twoSum(lst, target) == [0, 1]
