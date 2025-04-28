from collections import deque

def tree_by_levels(node):
    if node is None:
        return []

    value_list = []
    que = deque()
    que.append(node)
    
    while len(que) != 0:
        node = que.popleft()
        if node is None:
            continue
        value_list.append(node.value)
        que.append(node.left)
        que.append(node.right)
        
    return value_list

