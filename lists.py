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

############ INTERVIEW CAKE (1) ############

def highest_profit(lst):
  # hp = 0
  # i = 0 
  
  # while i < len(lst) - 1:
  #   j = i + 1
  #   right = lst[j]
  #   left = lst[i]

  #   if right > left: 
  #     curr_delta = right - left
  #     if curr_delta > hp: 
  #       hp = curr_delta
  #       j += 1
   
  #   i += 1
  
  # return hp

# greedy approach
    min_price = lst[0]
    hp = 0

    for curr_price in lst: 
        min_price = min(min_price, curr_price)
        
        potential_profit = curr_price - min_price

        max_profit = max(max_profit, potential_profit)

    return max_profit

## Tests ##    
lst = [10, 7, 5, 6, 12, 2]
high_profit(lst) == 7

############ INTERVIEW CAKE (2) ############

def get_prod_except_int(ints_lst):
  prod_lst = []
  i = 0
  
  while i < len(ints_lst):
    except_lst = []
    except_lst.extend(ints_lst[:i])
    except_lst.extend(ints_lst[i+1:])
    prod = reduce(lambda x,y: x*y, except_lst)
    prod_lst.append(prod)
    i += 1
    
  return prod_lst
  
def get_prod_except_int2(ints_lst):  
  prod_lst = [None]*len(ints_lst)
  
  prod_for = 1
  for i in xrange(len(ints_lst)):
    prod_lst[i] = prod_for
    prod_for *= ints_lst[i]
  
  print "prod_before_idx", prod_lst 

  prod_back = 1
  i = len(ints_lst) -1
  while i >= 0:
    prod_lst[i] *= prod_back
    prod_back *= ints_lst[i] 
    i -= 1
  print "prod_final", prod_lst 
    
  return prod_lst
    
  
# Tests
print get_prod_except_int2([1,2,3,4]) == [24,12,8,6]
print get_prod_except_int2([-2,6,-3,2]) == [-36,12,-24,36]

############ INTERVIEW CAKE (3) ############

def high_prod_of_3(ints_lst):
  """Given a list of integers, find the highest product you can get from three of the integers."""

  


