# 路径类
class Path:
    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.length = length

# 跑步的状态类（指停留在哪个地标）
class RunState:
    def __init__(self, current_n, target_n, total_length=0, previous_state=None):
        self.current_n = current_n
        self.target_n = target_n
        self.total_length = total_length
        self.previous_state = previous_state
    
    # Cost Function 这里指总代价函数
    def cost(self):
        return self.total_length

    # Heuristic Function 启发函数，这里启发函数只要设计的比真实值小即可
    def heuristic(self):
        return 0.5  # 由于我们很难得知每一条路和地标直接有什么关系，所以这里值设为 0 即可，或者是小于1的值（因为在例子中路径都是整数）
    
    # f值 指代价函数和启发函数之和
    def f(self):
        return self.cost() + self.heuristic()
    
    # 返回这个状态是否抵达终点状态
    def arrived(self):
        return self.current_n == self.target_n

    # 返回下个状态集
    def next_states(self, paths):
        if self.arrived():
            return []
            
        states = []
        for path in paths:
            if path.start == self.current_n:
                states.append(
                    RunState(path.end, self.target_n, self.total_length + path.length, self)
                )
        return states