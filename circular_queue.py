class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {removed}")
        return removed

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Queue contents:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# 👇 Example usage
if __name__ == "__main__":
    cq = CircularQueue(5)

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.display()

    cq.dequeue()
    cq.dequeue()
    cq.display()

    cq.enqueue(50)
    cq.enqueue(60)
    cq.display()

    cq.enqueue(70)  # Should show "Queue is full"
