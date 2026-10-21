stack = []

def push(item):
    stack.append(item)

def pop_item():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Removed:", stack.pop())

def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top item:", stack[-1])

def display():
    print("Stack:", stack)

for item in [10, 20, 30, 40, 50]:
    push(item)
peek()
pop_item()
pop_item()
display()
