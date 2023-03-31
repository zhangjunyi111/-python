tree = {}


def buildtree(nodes, parents):
    for i in range(len(nodes)):
        node_key = nodes[i]
        parent_key = parents[i]
        if node_key not in tree:
             tree[node_key] = []

        if parent_key == 0:
            continue

        parent_list=None
        if parent_key in tree:
            parent_list = tree[parent_key]
        else:
            parent_list = []
            tree[parent_key] = parent_list
        parent_list.append(node_key)


def rm_node(rmid):
    children = tree.get(rmid)
    if len(children) == 0:
        tree.pop(rmid)
        return

    for child in children:
        rm_node(child)
    tree.pop(rmid)


if __name__ == "__main__":
    num = int(input())
    nodes = []
    parents = []
    for i in range(num):
        line = list(map(int, input().split()))
        nodes.append(line[0])
        parents.append(line[1])
    rmid = int(input())
    buildtree(nodes, parents)
    rm_node(rmid)
    for key in tree.keys():
        print(key, end=" ")
