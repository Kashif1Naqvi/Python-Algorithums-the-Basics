from collections import deque

queue = deque()

queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft()
print(queue)

# output deque([3, 4, 5])