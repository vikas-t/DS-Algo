#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/expression-tree/1

# In the question the tree is already formed, we need to parse and evaluate
# the expression returning the result as an integer

def isOperator(op):
    return op in "+-/*"

def evalExpressionTree(root):
    """
    Follow the standard postfix to expression evaluation method
    If the expression is an operand keep pushing it on the stack, if the 
    expression is an operator pop the next two values from the stack
    and calculate the sub result. Push the sub result on the stack again and
    follow the same
    """
    expList = []
    traverseExpression(root, expList)
    # Traverse the tree in postorder
    
    stack = []
    for ch in expList:
        if isOperator(ch):
            r = int(stack.pop())
            l = int(stack.pop())
            if ch == "-":
                subRes = l-r
            elif ch == "/":
                subRes = l/r
            elif ch == "+":
                subRes = l+r
            elif ch == "*":
                subRes = l*r
            else:
                raise Exception("Invalid expression")
            stack.append(subRes)
        else:
            stack.append(ch)
    return subRes
            

def traverseExpression(root, res):
    """
    Parse the tree in postorder which will result in postfix expression
    """
    if root == None:
        return
    traverseExpression(root.left, res)
    traverseExpression(root.right, res)
    res.append(root.data)