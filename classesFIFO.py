class QueueError(Exception):  # Choose base class for the new exception.
    #  Write code here
    def _init__(self):
        pass
    def __str__(self):
        return "Queue error"

class Queue:
    def __init__(self):
        # Write code here
        self.__stk = []

    def put(self, elem):
        # Write code here
        self.__stk.append(elem)

    def get(self):
        val = self.__stk[0]
        del self.__stk[0]
        return val


que = Queue()
que.put(1)
que.put("dog")
que.put(False)


try:
    for i in range(4):
        print(que.get())
except:
    print(QueueError())
