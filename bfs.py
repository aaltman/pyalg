
class BfsGraphNode:
    adj = []
    val = None

    def __init__(self, newval, new_adj_list):
        self.val = newval

    def __str__(self):
        return str(self.val)

    def __iter__(self):
        return iter(self.adj)

    def add_adj(self, new_adj_node):
        self.adj.append(new_adj_node)


def bfs(graph_node, already_printed = None):
    print(graph_node)

    if already_printed is None:
        already_printed = [graph_node]

    for node in graph_node:
        if node in already_printed:
            continue

        print(", " + str(node))
        already_printed.append(node)

    for node in graph_node:
        if node not in already_printed:
            bfs(graph_node, already_printed)


node_0 = BfsGraphNode(0, [])
node_1 = BfsGraphNode(1, [])
node_2 = BfsGraphNode(2, [])
node_3 = BfsGraphNode(3, [])
node_4 = BfsGraphNode(4, [])
node_5 = BfsGraphNode(5, [])


def make_symmetrically_adjacent(left, right):
    left.add_adj(right)
    right.add_adj(left)


make_symmetrically_adjacent(node_0, node_1)
make_symmetrically_adjacent(node_0, node_2)
make_symmetrically_adjacent(node_2, node_3)
make_symmetrically_adjacent(node_2, node_4)
make_symmetrically_adjacent(node_3, node_4)
make_symmetrically_adjacent(node_2, node_5)
make_symmetrically_adjacent(node_4, node_5)


bfs(node_0)
