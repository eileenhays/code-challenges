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
    count = 0
    b = list(b)
    
    for char in a:
        if char in b: 
            b.remove(char) # make it mutable
        else: # char not in b 
            count += 1
            
    count += len(b)   
    return count

# a = raw_input().strip()
# b = raw_input().strip()

# print number_needed(a, b)

# Tests
print number_needed('cde', 'abc') == 4 
print number_needed('abbc', 'bda') == 3 

## Hash Tables: Ransom Note

from collections import defaultdict

def ransom_note2(m, n, magazine, ransom):
    if n > m:
        return False
    
    mag_dict = defaultdict(int)
    
    for word in magazine:
        mag_dict[word] += 1
    
    for word in ransom:
        if mag_dict[word] == 0:
            return False
        mag_dict[word] -= 1
        
    return True 


# m, n = map(int, raw_input().strip().split(' '))
# magazine = raw_input().strip().split(' ')
# ransom = raw_input().strip().split(' ')
# answer = ransom_note(magazine, ransom, m, n)
# if(answer):
#     print "Yes"
# else:
#     print "No"

# Tests
print ransom_note2(6, 4, 'give me one grand today night', 'give one grand today') == True
print ransom_note2(6, 5, 'two times three is not four', 'two times two is four') == False

## Linked Lists: Detect a Cycle

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
"""
 
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head, visited=[]):

    node = head
    
    if node == None:
        return False
    elif node.next == None:
        return False
    elif node in visited:
        return True
    
    visited.append(node)
    return has_cycle(node.next, visited)

# Tests
no_cycle_ll = Node(4, Node(5, Node(6, None)))
node_1 = Node(1, None)
node_2 = Node(2, None) 
node_3 = Node(3, None)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_2  
cycle_ll = node_1

print has_cycle(no_cycle_ll) == False
print has_cycle(cycle_ll) == True




