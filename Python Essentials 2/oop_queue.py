class QueError(Exception):
        pass

class Queue:
    def __init__(self):
        self.__queue_list = []

    def get_queue(self):
        return self.__queue_list

    def put(self, val):
        self.__queue_list.insert(0,val)

    def get(self):
        if not self.__queue_list:
            raise QueError("Queue error")
        else:
            val = self.__queue_list[-1]
            del self.__queue_list[-1]
            return val
        
    def isempty(self):
        return len(self.__queue_list) == 0
           

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")



