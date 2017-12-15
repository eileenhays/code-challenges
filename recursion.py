# Add two binary numbers together to return another binary number

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        
        if a[-1] == '1' and b[-1] == '1': # two 1's return 0 and carry 1 to previous column 
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0': # two 0's return 0 
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else: # one 0 and one 1 
            return self.addBinary(a[:-1], b[:-1]) + '1'

## Tests ##
test1 = Solution()
test1.addBinary('1001', '11') == '1100'