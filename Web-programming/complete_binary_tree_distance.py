"""
완전이진트리가 있을 때, 두 노드 간의 거리를 구하는 프로그램을 작성하시오.
노드 간의 거리는 한 노드에서 다른 노드로 거치는 간선 수의 합을 의미한다.
"""

def to_parent_node(node: int) -> int:
    if(node==1):
        return 1
    else:
        return node//2

node1, node2 = map(int, input().split(" "))
cnt = 0

while(node1!=node2):
    if(node1 > node2):
        node1 = to_parent_node(node1)
    else:
        node2 = to_parent_node(node2)

    cnt += 1

print(cnt)