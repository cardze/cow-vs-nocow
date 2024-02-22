import time

def without_cow():
    data = [0] * 100000
    for i in range(100000):
        data[i] = i

def with_cow():
    data = [0] * 100000
    for i in range(100000):
        data = data[:i] + [i]

start_time = time.time()
without_cow()
end_time = time.time()
print("Time without copy on write:", end_time - start_time)

start_time = time.time()
with_cow()
end_time = time.time()
print("Time with copy on write:", end_time - start_time)