

from  Assessment1 import *
import hashlib
import random
import string



"""
SOUL SALE AGREEMENT

THIS AGREEMENT is made this ____ day of ________, 20, by and between the undersigned (hereinafter referred to as the “Seller”) and Dr. Nick Dalton (hereinafter referred to as the “Buyer”).

WHEREAS, the Seller desires to sell and the Buyer desires to purchase the Seller’s soul upon the Seller’s death.
To agree to these terms of this contract the Seller will look at the course code below. 

NOW, THEREFORE, in consideration of the mutual promises contained herein, the parties agree as follows:

	1.	SALE OF SOUL
	•	The Seller hereby agrees to sell, transfer, and convey all rights, title, and interest in and to their soul to the Buyer upon the moment of the Seller’s death.
	2.	CONSIDERATION
	•	In exchange for the Seller’s soul, the Buyer agrees to provide the Seller with eternal fame, glory, and an unlimited supply of chocolate (or other preferred treats).
	3.	WARRANTIES
	•	The Seller warrants that they are of sound mind and legal age to enter into this agreement and that they have not made any prior agreements regarding the sale of their soul.
	4.	GOVERNING LAW
	•	This Agreement shall be governed by and construed in accordance with the laws of the Universe.
	5.	MISCELLANEOUS
	•	This Agreement constitutes the entire understanding between the parties and may not be amended except in writing signed by both parties.

"""

























#------------------------DO NOT CHANGE CODE BELOW------------------------
import inspect


def get_static_hash(input_string):
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    hash_object.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()

    return hash_hex

global_student_mark = 0
maxPossible_student_mark = 0

def test_question1_A():
    general_testQuestion("Q1a", Question1_a, "6978ce3c36b33c2")
def testQuestion1_DO_NOT_ALTER_THIS_CODE( ):
    def Question1Example(d, K: int):  # DO NOT ALTER THIS CODE
        for i in range(K):
            d[len(d) // 2] = 6

    old = deque()
    global d
    GENERAL_DO_NOT_ALTER_THIS_CODE(d, "Q1b", Question1Example, old, "dad4078")


def test_question1_C():
    general_testQuestion( "Q1c",Question1_c , "f3c1bfeb660" )

#-------------------
def test_question2_A():
    general_testQuestion("Q2a", Question2_a, "bad775d58b24")

def testQuestion2_DO_NOT_ALTER_THIS_CODE( ):
    def Question2Example(Q2, K:int ): # Do NOT Alter this code
        for i in range(K): # Do NOT Alter this code
            Q2.insert(0, i)  # Do NOT Alter this code

    old = list()
    global Q2
    GENERAL_DO_NOT_ALTER_THIS_CODE(Q2, "Q2b", Question2Example, old, "48c8bf4ab7" , SIZE= 5_000)

def test_question2_C():
    general_testQuestion("Q2c", Question2_c, "8d266f3c1bfeb6")



#--------------
def GENERAL_DO_NOT_ALTER_THIS_CODE( collect, questionName , oldTestCode , old , correctType, SIZE = 500_000 ):
    global global_student_mark
    global  maxPossible_student_mark

    random_ints = [random.randint(1, 100000) for _ in range(SIZE)]
    for it in random_ints:
        collect.append( it )
        old.append( it )

    K = len(collect)//5
    print(f"Testing  {questionName}")
    start_time = time.time()
    oldTestCode( collect, K )
    end_time = time.time()
    student_version_time = end_time - start_time
    print(f'Time for your version = {student_version_time}')

    start_time_old = time.time()
    oldTestCode(old, K)
    end_time_old = time.time()
    old_version_time = end_time_old - start_time_old
    print(f'Time for orignal version of {questionName} = {old_version_time}')
    speed_increase = old_version_time/student_version_time
    if speed_increase < 5 :
        result  = "(No change)"
    else:
        result = "{:.0f}! Great".format(speed_increase)

    print(f'{ questionName }Speed increase factor {result}')
    studentChoiceName = collect.__class__.__name__
    MARK = 10
    maxPossible_student_mark += MARK
    if correctType in get_static_hash(studentChoiceName) :

        global_student_mark += MARK
        print( f"This is correct {MARK} Marks, Total {global_student_mark}")
    else:
        print(f"This is not correct ")


#---------------
def general_testQuestion( name, function ,  correctHash  ):
    global global_student_mark, maxPossible_student_mark

    ans = function()
    hsh = get_static_hash(ans)
    MARK = 5
    maxPossible_student_mark += MARK

    if  correctHash in hsh :

        global_student_mark += MARK

        print(f"{name} is correct {MARK} Marks, Total {global_student_mark}")
    else:
        print(f"{name} {ans} is not correct ")

def generate_random_string(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def GENERAL_DO_NOT_ALTER_THIS_CODE_WITH_ADD(collect, questionName, addCode, newFindCode , origCollec,
                                            oldAddCode, oldFindCode, correctTypes:list,
                                            SIZE = 500_000, MAKE_STRINGS=False ):
    global global_student_mark
    global  maxPossible_student_mark

    if MAKE_STRINGS == True:
        random_ints = [ generate_random_string(10) for _ in range(SIZE)]
    random_ints = [random.randint(1, 100000) for _ in range(SIZE)]

    for it in random_ints:
        addCode(  collect, it  )
        oldAddCode(origCollec, it )

    K = len(collect)//5
    print(f"Testing  {questionName}")
    start_time = time.time()
    for it in random_ints:
        newFindCode( collect, it  )
    end_time = time.time()
    student_version_time = end_time - start_time
    print(f'Time for your version = {student_version_time}')

    start_time_old = time.time()
    for it in random_ints:
        oldFindCode( origCollec, it  )
    end_time_old = time.time()
    old_version_time = end_time_old - start_time_old
    print(f'Time for orignal version of {questionName} = {old_version_time}')
    speed_increase = old_version_time/student_version_time

    if speed_increase < 5 :
        result  = "(No change)"
    else:
        result = "{:.0f}! Great".format(speed_increase)

    print(f'{ questionName }Speed increase factor {result}')
    studentChoiceName = collect.__class__.__name__
    MARK = 10
    maxPossible_student_mark += MARK
    for correctType in correctTypes:
        if correctType in get_static_hash(studentChoiceName) :
            global_student_mark += MARK
            print( f"This is correct {MARK} Marks, Total {global_student_mark}")
            return
        else:
            print(f"This is not correct ")


def test_question3_A():
    general_testQuestion("Q3a", Question3_a, "b244e6697")
def test_question3_C():
    general_testQuestion("Q3c", Question3_c, "7863127d")
def testQuestion3():
    def Question3ExampleADD_ORG(Q3, item: int):
        # OK TO CHANGE THE CODE BELOW TO HELP
        Q3.append(item)

    def Question3ExampleFind_ORG(Q3, What):
        # OK TO CHANGE THE CODE BELOW TO HELP
        for it in Q3:
            if it == What:
                return True
        # end for
        return False  # not found

    origCollec = list()

    GENERAL_DO_NOT_ALTER_THIS_CODE_WITH_ADD(Q3, "Q3b", Question3ExampleADD,
                                            Question3ExampleFind, origCollec,
                                            Question3ExampleADD_ORG, Question3ExampleFind_ORG,
                                            [ "29e4230b", "e903f3d812c"], 10_000  )

def testQuestion4():
    origCollecQ4 = list()  # [ "fhfh" , "djdjd", "wewew"]
    Q4_index = list()  # [ 0, 1, 2]

    def Question4ExampleADD_ORG(Q4, item: str):
        # OK TO CHANGE THE CODE BELOW TO HELP
        Q4.append(item)
        Q4_index.append(len(Q4))

    # So if user asks for What =  "djdjd" return 1
    def Question4ExampleFind_ORG(Q4, What):
        # OK TO CHANGE THE CODE BELOW TO HELP
        index = 0
        for it in Q4:
            if it == What:
                return index
            index += 1
        # end for
        return -1  # not found
    global  Q4

    GENERAL_DO_NOT_ALTER_THIS_CODE_WITH_ADD(Q4, "Q4b", Question4ExampleADD,
                                            Question4ExampleFind, origCollecQ4,
                                            Question4ExampleADD_ORG, Question4ExampleFind_ORG,
                                            [ "0ad70b1acd" ], 10_000  , True  )


def test_question4_A():
    general_testQuestion("Q4a", Question4_a, "38098e02e")


def test_question4_C():
    general_testQuestion("Q4c", Question4_c, "ed7863127d680")

def testQuestion5():
    questionName = "Q5"
    def Question5AddOriginal(Q5a, whattoAdd_A, Q5b, whatToAdd_B):
        # OK TO change the code below to help
        Q5a.append(whattoAdd_A)
        Q5b.append(whatToAdd_B)

    # return a itterable collection of everything in A which is in B
    # Order is not important in the collection
    def Question5FindOriginal(Q5a_, Q5b_):
        incommon = [ ]

        for a in Q5a_:
            for b in Q5b_:
                if a == b:
                    if a not in incommon:
                        incommon.append(a )
                    # end if
                # end if
            # end for
        # end for


        return incommon

    def timeThisCode( A_Q5Findcommon , collectionA, collectionB ):
        TIMES = 3
        print(hash(tuple(collectionA)), hash(tuple(collectionB)))
        start_time = time.time()
        r = [ ]

        for it in range(TIMES) :
            r = A_Q5Findcommon(collectionA, collectionB)
        #end for
        end_time = time.time()
        version_time = end_time - start_time
        return (version_time,r )


#start of function
    global  Q5a , Q5b
    global  maxPossible_student_mark, global_student_mark

    orgCollectionQ5a = deque()
    orgCollectionQ5b = deque()

    SIZE = 10_000
    collectionA = [ generate_random_string(10) for _ in range(SIZE)]
    collectionB = [generate_random_string(10) for _ in range(SIZE)]
    collectionB = [item for item in collectionB if item not in collectionA]
    collectionA = [item for item in collectionA if item not in collectionB]

    incommon = [generate_random_string(10) for _ in range(SIZE // 100)]
    collectionA = collectionA + incommon
    collectionB = collectionB + incommon
    random.shuffle(collectionA)
    random.shuffle(collectionB)

    #print( len(collectionA ), len( collectionB ))
    assert len(collectionA )== len( collectionB )

    for a in range( len(collectionA)):
        Question5Add( Q5a , collectionA[ a ], Q5b, collectionB[a] ) # call studen version
        Question5AddOriginal(orgCollectionQ5a, collectionA[a], orgCollectionQ5b, collectionB[a])

    # print("hash after adding, " , hash(tuple(orgCollectionQ5a)), hash(tuple(orgCollectionQ5b)))
    orignalCommon = [ ]
    #print(f"Testing  {questionName} Orignal version")

    (orignalTime,orignal_common)  = timeThisCode(Question5FindOriginal, orgCollectionQ5a,orgCollectionQ5b  )
    print(f'Time for original version = {orignalTime}')
    print(f"Testing  {questionName} Your version {len(orignal_common)} ")
    (studentTime, student_Items) = timeThisCode(Question5Find, Q5a, Q5b)
    print(f'Time for your version = {studentTime} {len(student_Items)}')
    orignal_common.sort( )
    student_Items.sort( )

    #print( " Org, student, common" , len(orignal_common) , len(student_Items ), len(incommon ) )

    if len( orignal_common ) != len( student_Items ):
        print(f' the number of items you returned is different from the original {len( orignal_common )} you had {len( student_Items )}')

    if orignal_common != student_Items:
        print(f'Your items are not the same ######')
    else:
        print('Items are the same.')

    speed_increase = orignalTime / studentTime

    if speed_increase < 5:
        result = "(No change)"
    else:
        result = "{:.0f}! Great".format(speed_increase)

    print(f'{questionName}Speed increase factor {result}')
    studentChoiceName = Q5a.__class__.__name__

    MARK = 10
    maxPossible_student_mark += MARK

    if "f7acf9e811" in get_static_hash(studentChoiceName):

        global_student_mark += MARK

        print(f"This is correct {MARK} Marks, Total {global_student_mark}")
        if speed_increase < 5 :
            print(f"WARNING your speed increase is low {speed_increase}, which means your using the correct collection in the wrong way ( fix this please) ")
    else:
        print(f"This is not correct ")
#end of function

def test_question5_A():
    general_testQuestion("Q5a", Question5_a, "643a4ce3ae3")


def test_question5_C():
    general_testQuestion("Q5c", Question5_c, "266f027")

def test_question6():
    general_testQuestion("Q6", Question6, "04e6d6ffc")

def test_question7():
    general_testQuestion("Q7", Question7, "3c1bfeb66")

def test_question8():
    general_testQuestion("Q8", Question8, "a82d5010738")

import inspect
def test_question9():
    global global_student_mark , maxPossible_student_mark
    source_code = inspect.getsource(Question9)
    MARK = 5
    maxPossible_student_mark += MARK
    result = Question9()

    if "time.time(" in  source_code and result > 0 :
        global_student_mark += MARK
        print("Q9 your code might be correct!")
    else:
        print("Q9 your code might be incorrect,  only a human can be sure.")

def test_question10():
    print("A human will mark this")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_question1_A()
    testQuestion1_DO_NOT_ALTER_THIS_CODE()
    test_question1_C()

    test_question2_A()
    testQuestion2_DO_NOT_ALTER_THIS_CODE()
    test_question2_C()

    test_question3_A()
    testQuestion3()
    test_question3_C()

    test_question4_A()
    testQuestion4()
    test_question4_C()

    test_question5_A()
    testQuestion5()
    test_question5_C()

    test_question6()
    test_question7()
    test_question8()

    test_question9()

    print(f"Final Mark {global_student_mark} out of {maxPossible_student_mark}")



