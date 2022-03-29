import os
import sys
import math

from PriorityQueue import PriorityQueue
from KlotskiState import State

def klotski(origin_state_list, target_state_list, col, row):
    expanded_state_set = set()
    
    # Compute path with two index 曼哈顿距离
    def manhattan_distance(current_idx, target_idx):
        current_x, current_y = current_idx // col, current_idx % row
        target_x, target_y = target_idx // col, target_idx % row
        dx = math.fabs(target_x - current_x)
        dy = math.fabs(target_y - current_y)
        return int(dx + dy)
    
    priorityq = PriorityQueue()
    current_state = State(origin_state_list, target_state_list, manhattan_distance, -1)
    priorityq.push(current_state.f(), current_state)

    # 类似DFS，只不过队列换成优先队列，即可实现A*算法
    while(current_state.heuristic() != 0):
        f, current_state = priorityq.pop()
        for state in current_state.next_states():
            if state.string() not in expanded_state_set:
                priorityq.push(state.f(), state)
                expanded_state_set.add(state.string())

    # 解题路径（以字符串形式)
    process = []
    state = current_state
    while(state.previous_state):
        process.append(state.string())
        state = state.previous_state 
    process.append(state.string())
    process.reverse()

    return current_state.cost(), process

if __name__ == '__main__':
    args = sys.argv[1:]
    try:
        input_path = args[0]
        if os.path.exists(input_path):
            try:
                wf = open('./output/klotski_output.txt', 'w')
            except:
                print('打开输出文件失败')
                exit(-1)
            target_state = [int(i) for i in args[1]]
            col, row = int(args[2]), int(args[3])
            with open(args[0]) as f:
                strs = f.readlines()
                origin_states = [[int(i) for i in str.strip('\n')] for str in strs]
                for origin_state in origin_states:
                    f, process = klotski(origin_state, target_state, col, row)
                    wf.write(str(f))
                    wf.write(' 状态转移过程： ')
                    for state_str in process:
                        wf.write(state_str)
                        wf.write(' ')
                    wf.write('\n\n')
        else:
            origin_state = [int(i) for i in args[0]]
            target_state = [int(i) for i in args[1]]
            col, row = int(args[2]), int(args[3])
            f, process = klotski(origin_state, target_state, col, row)
            print(f, '状态转移过程： ')
            for state_str in process:
                print(state_str, end=' ')
            print()

    except:
        print('输入格式错误!!! 请按照格式输入：源状态/文件 目标状态 col row')