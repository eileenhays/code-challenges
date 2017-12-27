############# DATA STRUCTURES ##################

### Arrays: Left Rotation
def array_left_rotation(a, n, k):
    times = 0
    
    while times < k: 
        first_item = a.pop(0)
        a.append(first_item)
        times += 1
    
    return a

def array_left_rotation2(a, n, k):
	new_a = []
	i = 0

	for i in range(n): 
		new_idx = (i + k) % n
		new_a.append(a[new_idx])
		print new_a

	return new_a
        

# n, k = map(int, raw_input().strip().split(' '))
# a = map(int, raw_input().strip().split(' '))
        
# answer = array_left_rotation(a, n, k);
# print ' '.join(map(str,answer))

# Tests
print array_left_rotation2([1,2,3,4,5], 5, 4) == [5,1,2,3,4] 
print array_left_rotation2([4, 0, 3], 3, 1) == [0,3,4]

### Strings: Making Anagrams
def number_needed(a, b):
    pass

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

# # Tests
print number_needed('cde', 'abc') == 4 
