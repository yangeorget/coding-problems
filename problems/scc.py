class SCC:
    """
    Strongly connected components using Tarjan's algorithm.
    See https://practice.geeksforgeeks.org/problems/strongly-connected-component-tarjanss-algo-1587115621/1/
    """

    index = 0  # global counter that will be only incremented

    def compute_sccs(self, v, graph):
        node_stack = []  # the stack that will be used to build the SCC
        on_stack = [
            False for i in range(0, v)
        ]  # to detect in constant time if a node is on the stack
        indices = [-1 for i in range(0, v)]  # the DFS ordering of the nodes
        min_indices = [-1 for i in range(0, v)]  # smallest indices reachable by DFS
        sccs = []
        for i in range(0, v):
            if indices[i] == -1:
                self.connect(graph, i, node_stack, on_stack, indices, min_indices, sccs)
        return sorted(sccs)

    def connect(self, graph, i, node_stack, on_stack, indices, min_indices, sccs):
        indices[i] = min_indices[i] = self.index
        self.index += 1
        node_stack.append(i)
        on_stack[i] = True
        for j in graph[i]:
            if indices[j] == -1:  # this node has not been encountered yet
                self.connect(graph, j, node_stack, on_stack, indices, min_indices, sccs)
                min_indices[i] = min(min_indices[i], min_indices[j])
            else:  # this node has already been encountered
                if on_stack[j]:
                    min_indices[i] = min(min_indices[i], indices[j])
                else:
                    # this edge points to an already found SCC and must be ignored
                    pass
        if indices[i] == min_indices[i]:
            sccs.append(self.build_scc(i, node_stack, on_stack))

    def build_scc(self, i, node_stack, on_stack):
        scc = []
        while True:
            j = node_stack.pop()
            on_stack[j] = False
            scc.append(j)
            if i == j:
                break
        return sorted(scc)
