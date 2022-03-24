class Parentheses:
    """
    Given a string S consisting of opening and closing parenthesis '(' and ')',
    find length of the longest valid parenthesis substring.
    See https://practice.geeksforgeeks.org/problems/longest-valid-parentheses5657/1/
    """

    def max_length(self, string):
        starts = [-1]  # TODO remove
        max_len = 0
        for i in range(0, len(string)):
            if string[i] == "(":
                starts.append(i)
            else:
                if len(starts) != 0:
                    starts.pop()
                if len(starts) != 0:
                    cur_len = i - starts[-1]
                    max_len = max(max_len, cur_len)
                else:
                    starts.append(i)
        return max_len
