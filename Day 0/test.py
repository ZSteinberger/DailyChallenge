
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class PriorityList:
    def __init__(self):
        self.headval = None



#TODO: I NEED A LINKED LIST FOR MY QUEUE
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    queries.sort()
    queryPriorityQueue = PriorityList()
    currValue = 0
    maxValue = 0
    for j in range(len(queries)):
        # print(queries[j])
        # if(queryPriorityQueue.headval != None):
        #     print(queryPriorityQueue.headval.dataval)

        while queryPriorityQueue.headval != None and queryPriorityQueue.headval.dataval[0] < queries[j][0]:
            # print(queryPriorityQueue.headval.dataval[1])
            currValue -= queryPriorityQueue.headval.dataval[1]
            queryPriorityQueue.headval = queryPriorityQueue.headval.nextval
# if the Priority queue is empty or the current queries[j] needs to be popped before the last one append
        if queryPriorityQueue.headval == None:
            newNode = Node((queries[j][1],queries[j][2]))
            newNode.nextval = queryPriorityQueue.headval
            queryPriorityQueue.headval = newNode
            #7542539201
            #13908629997
            #13094989998
        else:
            prev = None
            test = queryPriorityQueue.headval
            while test != None:
                if(queries[j][1] <= test.dataval[0]):
                    print("HERE", queries[j][1], test.dataval[0])
                    newNode = Node((queries[j][1],queries[j][2]))
                    newNode.nextval = test
                    if prev != None:
                        prev.nextval = newNode
                    else:
                        queryPriorityQueue.headval = newNode
                    break
                prev = test
                test = test.nextval
            if test == None:
                newNode = Node((queries[j][1],queries[j][2]))
                newNode.nextval = prev.nextval
                prev.nextval = newNode
        currValue += queries[j][2]
        if currValue > maxValue:
            maxValue = currValue  

    return maxValue
#4000 30000
# N = 30000

#40 30
N = 30
X = [(29, 40, 787), (9, 26, 219), (21, 31, 214), (8, 22, 719), (15, 23, 102), (11, 24, 83), (14, 22, 321), (5, 22, 300), (11, 30, 832), (5, 25, 29), (16, 24, 577), (3, 10, 905), (15, 22, 335), (29, 35, 254), (9, 20, 20), (33, 34, 351), (30, 38, 564), (11, 31, 969), (3, 32, 11), (29, 35, 267), (4, 24, 531), (1, 38, 892), (12, 18, 825), (25, 32, 99), (3, 39, 107), (12, 37, 131), (3, 26, 640), (8, 39, 483), (8, 11, 194), (12, 37, 502)]
print(arrayManipulation(N, X))