from Queue import Queue
class Printer:
    def __init__(self):
        self.queue=Queue()
    def Enqueue(self,job):
        self.queue.Enqueue(job)
    def Dequeue(self):
        self.queue.Dequeue()
    def Peek(self):
        self.queue.Peek()
    def isEmpty(self):
        return self.queue.isEmpty()
    def Size(self):
        return self.queue.size()

    def Print(self):
        self.queue.Print()

if __name__=='__main__':

    p=Printer()
    p.Enqueue('ENGINEER')
    p.Enqueue('Doctor')
    p.Print()
    p.Dequeue()
    p.Print()
