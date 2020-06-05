import numpy as np
str1 = "GACTTAC"
str2 = "CGTGAATTCAT"

l = np.zeros(shape=(len(str1)+1, len(str2)+1))

# Get row
l[0][:] = np.array([-i for i in range(len(str2)+1)])
# Get column
l[:, 0] = np.array([-i for i in range(len(str1)+1)])




print(l[1:, 1:])
for idxs,items in enumerate(l[1:, 1:]):
    print(idxs, items)
    for idx,item in enumerate(items):
        print(idx, item)
        if str1[idxs] == str2[idx]:
            print(l)
            print(l[idxs-1][idx]-1)
            print(l[idxs][idx-1]-1)
            print(l[idxs-1][idx-1]+1)

            max_elem = max(l[idxs+1][idx]-1, l[idxs][idx+1]-1, l[idxs][idx]+1)
        else:
            print(l)
            print(l[idxs-1][idx]-1)
            print(l[idxs][idx-1]-1)
            print(l[idxs-1][idx-1]+1)

            max_elem = max(l[idxs+1][idx]-1, l[idxs][idx+1]-1, l[idxs][idx]-1)
        print("Element is :" + str(max_elem)) 
        l[idxs+1][idx+1] = max_elem

print(l)

"""for idx, item in items:
        print(idx, item)"""