# https://www.acmicpc.net/problem/1260
# (출처 없음)

import queue

input_str = (input()).split(" ")
N = int(input_str[0])
M = int(input_str[1])
V = int(input_str[2])
del input_str

# 초기 배열 할당
Graph = [list() for _ in range(N + 1)]

# 그래프 요소 채우기
for _ in range(M):
    input_str = (input()).split(" ")
    start_num = int(input_str[0])
    end_num = int(input_str[1])
    del input_str

    Graph[start_num].append(end_num)
    Graph[end_num].append(start_num)

[item.sort() for item in Graph]


# DFS
def DFS(_checklist, _item):
    print(_item, end=" ")
    for next_item in Graph[_item]:
        if _checklist[next_item] is False:
            _checklist[next_item] = True
            DFS(_checklist, next_item)

checklist = [False for _ in range(N + 1)]
checklist[V] = True
DFS(checklist, V)
print("")
del checklist

# BFS
checklist = [False for _ in range(N + 1)]
Q = queue.Queue()
Q.put(V)
checklist[V] = True

while Q.empty() is False:
    item = Q.get()
    print(item, end=" ")
    for next_item in Graph[item]:
        if checklist[next_item] is False:
            checklist[next_item] = True
            Q.put(next_item)
print("")

del checklist
del Q
