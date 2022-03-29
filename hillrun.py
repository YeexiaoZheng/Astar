import os
import sys

from PathRunState import Path, RunState
from PriorityQueue import PriorityQueue

def hillrun(K, paths, origin_n, target_n):
    Paths = []
    for path in paths:
        Paths.append(Path(path[0], path[1], path[2]))
    
    current_state = RunState(origin_n, target_n)
    priorityq = PriorityQueue()
    priorityq.push(current_state.f(), current_state)

    lengths = []
    runpaths = []

    # 循环K次找到K条路径
    for _ in range(K):
        if priorityq.empty():
            lengths.append(-1)
            continue
        
        # 循环找到一个路径
        f, current_state = priorityq.pop()
        while(not current_state.arrived()):
            for state in current_state.next_states(Paths):
                priorityq.push(state.f(), state)

            # 如果队列中没有元素了，直接break
            if priorityq.empty():
                break
            f, current_state = priorityq.pop()
        
        # 如果状态是达到终点，则将其添加到输出的列表中
        if current_state.arrived():
            lengths.append(current_state.cost())
            runpath = []
            state = current_state
            while(state.previous_state):
                runpath.append(state.current_n)
                state = state.previous_state
            runpath.append(state.current_n)
            runpath.reverse()
            runpaths.append(runpath)

    return lengths, runpaths

if __name__ == '__main__':
    args = sys.argv[1:]
    
    if len(args) > 0 and os.path.exists(args[0]):
        try:
            wf = open('./output/hillrun_output.txt', 'w')
        except:
            print('打开输出文件失败')
            exit(-1)

        with open(args[0]) as f:
            prob = int(f.readline().strip('\n'))
            
            for _ in range(prob):
                paths = []
                f.readline()
                line = f.readline()
                try:
                    N, M, K = tuple([int(i) for i in line.strip('\n').strip(' ').split(' ')])
                except:
                    print('格式输入错误')
                    exit(-1)

                for i in range(M):
                    line = f.readline()
                    paths.append([int(i) for i in line.strip('\n').strip(' ').split(' ')])
                
                try:
                    lengths, runpaths = hillrun(K, paths, N, 1)
                    for i in range(len(lengths)):
                        wf.write(str(lengths[i]))
                        wf.write(' 路径: ')
                        if i < len(runpaths):
                            for n in runpaths[i]:
                                wf.write(str(n))
                                wf.write(' ')
                        wf.write('\n')
                except Exception as e:
                    print(e, '格式输入错误')
                    exit(-1)
                wf.write('\n')
        wf.close()
        f.close()

    else:
        line = input('请输入N(地标数) M(路径数) K(最短路径数)\n')
        paths = []
        try:
            N, M, K = tuple([int(i) for i in line.strip('\n').strip(' ').split(' ')])
        except:
            print('格式输入错误')
            exit(-1)

        for i in range(M):
            line = input('请输入路径M条: 地标 地标 长度\n')
            paths.append([int(i) for i in line.strip('\n').strip(' ').split(' ')])

        try:
            lengths, runpaths = hillrun(N, M, K, paths, N, 1)
            for length, runpath in zip(lengths, runpaths):
                print(length, '路径: ', end='')
                for n in runpath:
                    print(n, end=' ')
                print()
        except:
            print('格式输入错误')
            exit(-1)