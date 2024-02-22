from lib.disk import Disk
from lib.data import Data

d = Disk(cow=False)
print(d)
idx1 = d.write(Data("data1"))
print(d)
idx2 = d.write(Data("data2"))
print(d)
print(idx1, idx2)
d.cow = False
d.update(Data("data3"), idx1)
print(d)
