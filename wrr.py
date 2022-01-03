# Python program to
# demonstrate queue implementation
# using list

# Initializing a queue
d1queue = []
d2queue = []
d3queue = []
d4queue = []

d0=0
d1=0
d2=0
d3=0

iterations =0

d1queue.append('p1')
d1queue.append('p2')
d1queue.append('p3')

d2queue.append('p1')
d2queue.append('p2')
d2queue.append('p3')

d3queue.append('p1')
d3queue.append('p2')
d3queue.append('p3')

d4queue.append('p1')
d4queue.append('p2')
d4queue.append('p3')

queue = { 0 : d1queue,
            1 : d2queue,
            2 : d3queue,
            3 : d4queue,
            }

weights = { 0 : 2,
            1 : 1,
            2 : 1,
            3 : 2,
            }

counter = { 0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            }

for x in range(4):
    for y in range(weights[x]):
        queue[x].pop(0)
        counter[x]=counter[x]+1
        iterations=iterations +1

print('number of packets forwarded from source D0 is')
print(counter[0])
print('number of packets forwarded from source D3 is')
print(counter[3])

print('Number of iterations')
print(iterations)

