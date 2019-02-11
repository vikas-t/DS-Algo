#!/usr/bin/python3
# Reverse stack

def insert(stack, v):
    if not stack:
        stack.append(v)
    else:
        t = stack.pop()
        insert(stack, v)
        stack.append(t)

def reverse(stack):
    if stack:
        t = stack.pop()
        reverse(stack)
        insert(stack, t)

# Driver code
x = [7,2,1,9,5]
reverse(x)
print(x)



# def isEmpty(stack):
#     if len(stack) == 0:
#         return True
#     return False

# def insertAtBottom(stack, item): 
#     if  isEmpty(stack):
#         stack.append(item) 
#     else: 
#         temp = stack.pop() 
#         insertAtBottom(stack, item) 
#         stack.append(temp)

# def reverse(stack): 
#     if not isEmpty(stack): 
#         temp = stack.pop() 
#         reverse(stack) 
#         insertAtBottom(stack, temp) 

# x = [1,2,3,4,5]
# reverse(x)
# print(x)