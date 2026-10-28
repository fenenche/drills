from collections import deque

def reverse_first(queue, k):
    if k <= 0 or k > len(queue):
        return queue
    stack = []
    for _ in range(k):
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    remaining_elements = len(queue) - k
    for _ in range(remaining_elements):
        queue.append(queue.popleft())
    return queue
my_list = deque([10, 20, 30, 40, 50]) 
k = 3

result = reverse_first(my_list, k)
print(list(result)) 