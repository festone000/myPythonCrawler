from collections import deque

queue = deque(['Eric','John','Michael'])
queue.append("Terry")
queue.append("Gaham")
queue.appendleft("First")
print(queue)
print('===============\n')
# queue.popleft()
queue.pop()
print(queue)
print('===============\n')
queue.popleft()

print(queue)