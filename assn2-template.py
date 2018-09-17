import time
import random

def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

def binsearch(List, lower, upper, target):
    mid = (lower + upper)//2
    if lower > upper:
        return -1
    if target == List[mid]:
        return 0
    elif target > List[mid]:
        return binsearch(List, lower, mid-1, target)
    elif target < List[mid]:
        return binsearch(List, mid+1, upper, target)

numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search
cnt = 0
length=len(numbers)-1
for target in targets:
    idx = binsearch(numbers,0,length,target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("Binary Search %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()
# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("Sequential Search %d: not found %d time %.6f" % (numoftargets, cnt, ts))
