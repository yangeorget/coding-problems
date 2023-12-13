from bisect import bisect_left


class Arrays:
    """
    Find the minimum number of insertions and deletions on the array A, required to make both the arrays A and B identical. The array B is sorted and its elements are distinct. 
    See https://practice.geeksforgeeks.org/problems/minimum-insertions-to-make-two-arrays-equal/1/
    """

    def min_ins_and_del(self, a, b, n, m):
        """
        
        """
        c = [x for x in a if self.in_sorted_array(b, x)]  # elements of a also in b
        length = self.lis_length(c)
        deletions = n - length
        insertions = m - length
        return deletions + insertions

    def in_sorted_array(self, b, x):
        i = bisect_left(b, x)
        return i < len(b) and b[i] == x

    def lis_length(self, a):
        """
        Returns the length of the longest increasing sequence.
        """
        s = []
        for x in a:
            if len(s) == 0 or x > s[-1]:
                s.append(x)
            else:
                i = bisect_left(s, x)  # s[i] >= x
        return len(s)
