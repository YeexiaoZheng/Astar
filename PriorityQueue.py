# 以小顶堆实现的优先队列
class PriorityQueue:

    # 队列中的节点
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            
    def __init__(self):
        self.heap = []

    # 入队时需要将末尾的节点与其父节点比较，递归，维护小顶堆
    def siftup(self, i):
        parent = (i - 1) // 2
        if self.heap[i].key < self.heap[parent].key and parent >= 0:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.siftup(parent)

    # 出队时会将heap末尾的节点放在队首，然后将其与子节点比较，递归，维护小顶堆
    def siftdown(self, i):
        n = len(self.heap)
        minimum, left, right = i, 2 * (i + 1) - 1, 2 * (i + 1)
        if ((left < n) and (self.heap[left].key < self.heap[minimum].key)):
            minimum = left
        if ((right < n) and (self.heap[right].key < self.heap[minimum].key)):
            minimum = right
        if minimum != i:
            self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
            self.siftdown(minimum)

    # 入队接口
    def push(self, key, value):
        self.heap.append(self.Node(key, value))
        self.siftup(len(self.heap) - 1)

    # 出队接口，弹出队首
    def pop(self):
        key, value = self.heap[0].key, self.heap[0].value
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.siftdown(0)
        return key, value
    
    # 队列长度接口
    def length(self):
        return len(self.heap)

    # 队列是否为空接口
    def empty(self):
        return len(self.heap) == 0