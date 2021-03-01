class QueueError(IndexError):  # Choose base class for the new exception.
    #  Write code here
    pass

class Queue:
    def __init__(self):
        # Write code here
        self.__stk = []

    def put(self, elem):
        # Write code here
        self.__stk.append(elem)

    def get(self):
        if len(self.__stk) == 0:
            raise QueueError
        else:
            val = self.__stk[0]
            del self.__stk[0]
            return val

    def getlist(self):
        return self.__stk

class SuperQueue(Queue):
    # Write new code here.
    def __init__(self):
        Queue.__init__(self)
        self.__count = 0

    def isempty(self):
        if self.__count == 0:
            return True
        else:
            return False

    def put(self, elem):
        self.__count +=1
        Queue.put(self, elem)

    def get(self):
        self.__count -=1
        return Queue.get(self)

    def getcount(self):
        return self.__count



que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
print(que.getlist())
print(que.getcount())

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
