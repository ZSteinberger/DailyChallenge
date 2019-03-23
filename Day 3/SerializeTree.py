# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# The following test should pass:

def serialize(node):
    stack = [node]
    output = ""
    while len(stack) != 0:
        curr = stack.pop()
        if curr != None:
            output += curr.val + " "
            stack.append(curr.right)
            stack.append(curr.left)
        else:
            output += "0 "
    return output

def deserialize(input):
    nodes = input.split()
    mode = True
    stack = []
    curr = root = Node(nodes[0])
    i = 1
    while i < len(nodes):
        if nodes[i] == "0":
            if mode:
                curr = stack.pop()
            mode = not mode
        else:
            if mode:
                curr.left = Node(nodes[i])
                stack.append(curr)
                curr = curr.left
            else:
                mode = not mode
                curr.right = Node(nodes[i])
                stack.append(curr)
                curr = curr.right
        i += 1
    return root
        

    

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(deserialize(serialize(node))))
print(serialize(node))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


    # return "root left left.left 0 0 0 right"

#             root
#         left    right
# left.left