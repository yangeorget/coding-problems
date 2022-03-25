ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class AlienDictionary:
    """
    Given a sorted dictionary of an alien language having n words and k letters,
    find the order of characters in the alien language.
    See https://practice.geeksforgeeks.org/problems/alien-dictionary/1
    """

    def find_order(self, arr, n, k):
        if n <= 1:
            return ALPHABET[:k]
        # we are going to compute a graph of letter indices where an edge means "smaller"
        smaller_graph = [[] for i in range(0, k)]
        nb_of_incoming_edges = [0 for i in range(0, k)]
        for i in range(0, len(arr) - 1):
            e = self.get_edge(arr[i], arr[i + 1])
            if e:
                if not e[1] in smaller_graph[e[0]]:
                    smaller_graph[e[0]].append(e[1])
                    nb_of_incoming_edges[e[1]] += 1
        nodes_with_no_incoming_edges = [
            i for i in range(0, k) if nb_of_incoming_edges[i] == 0
        ]
        # we compute a topological order using Kahn's algorithm
        order = []
        while len(nodes_with_no_incoming_edges) > 0:
            i = nodes_with_no_incoming_edges.pop()  # nobody's smaller than this node
            order.append(i)
            while len(smaller_graph[i]) > 0:
                m = smaller_graph[i].pop()
                nb_of_incoming_edges[m] -= 1
                if nb_of_incoming_edges[m] == 0:
                    nodes_with_no_incoming_edges.append(m)
        return "".join([ALPHABET[i] for i in order])

    def get_edge(self, word1, word2):
        """
        If the lexicographical order allows to find two letters x and y such that x != y,
        then returns the edge idx_x -> idx_y in the "smaller graph",
        where idx_x is the index of x in the alphabet and idx_y is the index of y in the alphabet.
        :param word1: a word
        :param word2: another word
        :return: the edge as a pair
        """
        for i in range(0, min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return ord(word1[i]) - ord("a"), ord(word2[i]) - ord("a")
        return None
