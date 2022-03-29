SPACE = 0

class State:
    def __init__(self, current_state_list, target_state_list, distance_function, last_cost, previous_state=None):
        self.previous_state = previous_state
        self.current_state_list = current_state_list
        self.target_state_list = target_state_list
        self.distance_func = distance_function
        self.last_cost = last_cost
    
    # Cost Function 代价函数 这里由于每一步代价均相同，为1即可
    def cost(self):
        return self.last_cost + 1
    
    # Heuristic Function 启发式函数 由传入的距离函数来设定状态转移到终点的总启发
    def heuristic(self):
        heuristic = 0
        for current_idx, value in enumerate(self.current_state_list):
            heuristic += self.distance_func(current_idx, self.target_state_list.index(value))
        return heuristic
    
    # 总的代价，为cost + heuristic
    def f(self):
        return self.cost() + self.heuristic()
    
    # 返回这个状态的下一个状态有哪些
    def next_states(self):
        next_states = []
        space_idx = self.current_state_list.index(SPACE)
        for idx in range(len(self.current_state_list)):
            # 找到SPACE和index的距离为1的index，交换其与SPACE，就是下一个状态
            if self.distance_func(idx, space_idx) == 1:
                t = self.current_state_list.copy()
                t[space_idx], t[idx] = t[idx], t[space_idx]
                next_states.append(State(t, self.target_state_list, self.distance_func, self.cost(), self))
        return next_states
    
    # 将状态list转为string
    def string(self):
        return ''.join([str(i) for i in self.current_state_list])