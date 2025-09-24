# Creating a stack
stack = []
stack = list()  # Anything will work

# Major operations of stacks: PUSH, POP

# PUSH operation
stack.append(1)

# POP operation
if stack:  # check if stack is empty
    stack.pop()
else:
    print("Underflow.")

# TOP: points to the top of the stack
