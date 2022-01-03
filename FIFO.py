# Python program to
# demonstrate queue implementation
# using list

# Initializing a queue
queue = []
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
# Adding elements to the queue
queue.append('a')
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
queue.append('a')
queue.append('e')
queue.append('f')
queue.append('g')
queue.append('h')
queue.append('i')
queue.append('j')
queue.append('a')
queue.append('a')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.__len__())
for x in range(10):
    item =queue[0]
    if item == 'a':
        a=a+1
    print(queue[0])
    queue.pop(0)
    

print("\nnumber of As")
print(a)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty
