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
print array_left_rotation2([1, 2, 3, 4, 5], 5, 4) == [5,1,2,3,4] 
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

# def has_cycle2(head):
#     curr = head
#     seen = set()
#     while curr:
#         if curr in seen:
#             return True
#         seen.add(curr)
#         curr = curr.next
#     return False

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


## Trees: Is this a Binary Search Tree? 
""" Node is defined as:
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    return check(root, min=0, max=10000)

def check(root, min, max):
    curr = root

    if curr == None: 
        return True

    if curr.data <= min or curr.data >= max:
        return False

    return check(curr.left, min, curr.data) and check(curr.right, curr.data, max)

def checkBST2(root):
    pass
    # return True if BST, or False if not

    # if left is not null 
    # check if it is smaller than root, if not, return False
    # if right is not null
    # check if it is larger than root, if not, return False
    # check the left side of the tree
        #set curr root to left, recurse and check each side
    # check the right side of the tree
        # set curr root to right, recurse and check each side 
    # return True
    # optimization: 
        # create a seen set to add node values as you traverse tree
        # check if the value is in seen before moving on
            #if it is, then return False because it is a duplicate

# Tests
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7a = Node(7)
node7b = Node(7)

node4.left, node4.right = node2, node6
node2.left, node2.right = node1, node3
node6.left, node6.right = node5, node7a
root_no_duplicates = node4

print checkBST(root_no_duplicates) == True

node4.left, node4.right = node2, node6
node2.left, node2.right = node1, node3
node6.left, node6.right = node5, node7a
node5.right = node7b
root_with_duplicates = node4

print checkBST(root_with_duplicates) == False


## Queues: A Tale of Two Stacks

"""
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue. (put)
2: Dequeue the element at the front of the queue. (pop)
3: Print the element at the front of the queue. (peek)
"""

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        return self.first[-1]
        
    def pop(self):
        self.first.pop()
        
    def put(self, value):
        self.first.insert(0, value)
        
def run_function(input):        
    queue = MyQueue()
    t = int(raw_input())
    for line in xrange(t):
        values = map(int, raw_input().split())
        
        if values[0] == 1:
            queue.put(values[1])        
        elif values[0] == 2:
            queue.pop()
        else:
            print queue.peek()

# Tests
# in_value = "10\n1 42\n2\n1 14\n3\n1 28\n3\n1 60\n1 78\n2\n2"
# out_value = "14\n14"
# print "Queue: ", run_function(in_value) == out_value


## Stacks: Balanced Parentheses 


def is_matched(expression):
    is_balanced = False
    front_brackets = ['[', '{', '(']
    back_brackets = [']', '}', ')']
    stack = []
    
    for char in expression:
        if char in front_brackets: 
            stack.append(char)
        elif char in back_brackets:
            if back_brackets.index(char) == front_brackets.index(stack[-1]):
                stack.pop()
            else: 
                return is_balanced
                
    if stack == []: 
        is_balanced = True
    
    return is_balanced

def is_matched2(expression):
    is_balanced = False
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in expression:
        if char in brackets.values(): 
            stack.append(char)
        else: # assuming that chars can only be one of the keys or values  
            if stack == []:
                return is_balanced
            elif brackets[char] == stack[-1]:
               stack.pop()
                
    if stack == []: 
        is_balanced = True
    
    return is_balanced

# Tests
print is_matched2("{[()]}") == True 
print is_matched2("{[(])}") == False 
print is_matched2("{{[[(())]]}}") == True 