import random
import time
import string
import bisect
from collections import deque
import matplotlib.pyplot as plt

# you will need to import matlibplot your self. don't forget to include

"""
Correct format strings for O(N?)  answers 

O(1)
O(LOG(N))
O(N) 
O(N LOG(N))
O(N**2)
O(N**2 LOG(N))
O(N**3) 
O(N**4) 
O(2**N)
O(N!) 

"""

# The developer left this code below

d = []  # #deque() #Alter this code


# more developer code was here but you don't need to know about it.

def Question1Example(d, K: int):  # DO NOT ALTER THIS CODE
    for i in range(K):  # Do not Alter this code
        d[len(d) // 2] = 6  # Do not Alter this code


def Question1_a():
    return "O(N)"  # If using N use N and if power use N**"


def Question1_c():
    return "O(1)"  # If using N use N and if power use N**"


# ------------------------------------------------
Q2 = deque()  # Alter this code


# the collection is filled in the assessment code.
# there is more code showing extensive use of list access.

def Question2Example(Q2, K: int):
    for i in range(K):  # Do not Alter this code
        Q2.insert(0, i)  # Do not Alter this code


def Question2_a():
    return "O(N)"  # If using N use N and if power use N**


def Question2_c():
    return "O(1)"  # If using N use N and if power use N**


# ------------------------------------------------
Q3 = set()  # OK to alter this


def Question3ExampleADD(Q3, item: int):
    # OK TO CHANGE THE CODE BELOW TO HELP
    Q3.add(item)


def Question3ExampleFind(Q3, What):
    # OK TO CHANGE THE CODE BELOW TO HELP
    return What in Q3


def Question3_a():
    return "O(N)"  # If using N use N and if power use N**


def Question3_c():
    return "O(1)"  # If using N use N and if power use N**


# ------------------------------------------------
Q4 = dict()


def Question4ExampleADD(Q4, item: str):
    # OK TO CHANGE THE CODE BELOW TO HELP
    Q4[item] = len(Q4)


# So if user asks for What =  "djdid" return 1
def Question4ExampleFind(Q4, What):
    # OK TO CHANGE THE CODE BELOW TO HELP
    return Q4.get(What, -1)


# What is the O notation for Question4ExampleFind
def Question4_a():
    return "O(N**2)"   # If using N use N and if power use N**"


# What is the O notation for Question4ExampleFind after you fix it
def Question4_c():
    return "O(N)"   # If using N use N and if power use N**"


Q5a = set()
Q5b = set()


def Question5Add(Q5a, whattoAdd_A, Q5b, whatToAdd_B):
    # OK TO change the code below to help
    Q5a.add(whattoAdd_A)
    Q5b.add(whatToAdd_B)


# return a itterable collection of everything in A which is in B
# Order is not important in the collection
def Question5Find(Q5a, Q5b):
    return list(Q5a & Q5b)


def Question5_a():
    return "O(?) If using N use N and if power use N**"


# What is the O notation for Question4ExampleFind after you fix it
def Question5_c():
    return "O(?)If using N use N and if power use N**"


Q6 = deque()


def Question6WhatIsMyONotation(items):  # DO NOT ALTER THIS CODE
    global Q6
    for it in items:
        Q6.insert(len(Q6) // 2, it)


def Question6():
    return "O(N**2)"  # If using N use N and if power use N**"


Q7 = set()


def Question7WhatIsMyONotation(item) -> bool:
    return item in Q7


def Question7():
    return "O(1)"  # If using N use N and if power use N**"


Q8 = list()  # don't change this


def Question8WhatIsMyONotation(Q8, item) -> int:
    index = bisect.bisect_left(Q8, item)

    if index < len(Q8) and Q8[index] == item:
        return index  # Item found
    else:
        return -1  # Item not found


def Question8():
    return "O(LOG(N))"  # If using N use N and if power use N**"


Q9 = [random.uniform(-100, 100) for _ in range(10000)]


def Question9WhatIsMyTime(Q9):
    Q9.sort()
    return Q9


def Question9():
    start_time = time.time()

    # Your code wraps around test
    global Q9
    Question9WhatIsMyTime(Q9)
    # Your code wraps around test

    end_time = time.time()
    return (end_time - start_time) * 1000


def Question10(lst):
    # your code here
    ys = lst
    xs = [x for x in range(len(ys))]

    plt.plot(xs, ys)
    plt.show()
    plt.close()


Question10(Question9WhatIsMyTime(Q9))
