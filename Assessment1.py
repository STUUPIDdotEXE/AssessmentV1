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
    return "O(N)"   # If using N use N and if power use N**


def Question2_c():
    return "O(1)"   # If using N use N and if power use N**


# ------------------------------------------------
Q3 = list()  # OK to alter this


def Question3ExampleADD(Q3, item: int):
    # OK TO CHANGE THE CODE BELOW TO HELP
    Q3.append(item)


def Question3ExampleFind(Q3, What):
    # OK TO CHANGE THE CODE BELOW TO HELP
    for it in Q3:
        if it == What:
            return True
    # end for
    return False  # not found


def Question3_a():
    return "O(N)"   # If using N use N and if power use N**


def Question3_c():
    return "O(?)If using N use N and if power use N**"


# ------------------------------------------------
Q4 = list()  # [ "fhfh" , "djdjd", "wewew"]
Q4_index = list()  # [ 0, 1, 2]


def Question4ExampleADD(Q4, item: str):
    # OK TO CHANGE THE CODE BELOW TO HELP
    Q4.append(item)
    Q4_index.append(len(Q4))


# So if user asks for What =  "djdjd" return 1
def Question4ExampleFind(Q4, What):
    # OK TO CHANGE THE CODE BELOW TO HELP
    index = 0
    for it in Q4:
        if it == What:
            return index
        index += 1
    # end for
    return -1  # not found


# What is the O notation for Question4ExampleFind
def Question4_a():
    return "O(?) If using N use N and if power use N**"


# What is the O notation for Question4ExampleFind after you fix it
def Question4_c():
    return "O(?)If using N use N and if power use N**"


Q5a = deque()
Q5b = deque()


def Question5Add(Q5a, whattoAdd_A, Q5b, whatToAdd_B):
    # OK TO change the code below to help
    Q5a.append(whattoAdd_A)
    Q5b.append(whatToAdd_B)


# return a itterable collection of everything in A which is in B
# Order is not important in the collection
def Question5Find(Q5a, Q5b):
    incommon = []

    for a in Q5a:
        for b in Q5b:
            if a == b:
                if a not in incommon:
                    incommon.append(a)
                # end if
            # end if
        # end for
    # end for
    return incommon


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
    return "O(?) If using N use N and if power use N**"


Q7 = set()


def Question7WhatIsMyONotation(item) -> bool:
    return item in Q7


def Question7():
    return "O(?) If using N use N and if power use N**"


Q8 = list()  # don't change this


def Question8WhatIsMyONotation(Q8, item) -> int:
    index = bisect.bisect_left(Q8, item)

    if index < len(Q8) and Q8[index] == item:
        return index  # Item found
    else:
        return -1  # Item not found


def Question8():
    return "O(?) If using N use N and if power use N**"


Q9 = [random.uniform(-100, 100) for _ in range(10000)]


def Question9WhatIsMyTime(Q9):
    return Q9.sort()


def Question9():
    # Your code wraps around test
    global Q9
    Question9WhatIsMyTime(Q9)
    # Your code wraps around test
    return -1


def Question10():
    # your code here
    pass
