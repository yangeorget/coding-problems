class Parentheses:
    """
    Given a string S consisting of opening and closing parenthesis '(' and ')',
    find length of the longest valid parenthesis substring.
    See https://practice.geeksforgeeks.org/problems/longest-valid-parentheses5657/1/
    """

    def max_length(self, string):
        """
        The idea is to maintain a list of parenthesis indices.
        The first index corresponds to the last extra closing parenthesis,
        while the next ones all correspond to opening parenthesis (not closed yet).
        """
        starts = []
        max_len = 0
        # without loss of generality and without modifying the result,
        # we can add an extra closing parenthesis at the beginning of the string
        for i, p in enumerate(")" + string):
            if p == "(":
                starts.append(i)
            else:
                if len(starts) <= 1:
                    starts = [i]
                else:
                    starts.pop()
                    max_len = max(max_len, i - starts[-1])
        return max_len
