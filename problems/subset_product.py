from bisect import bisect


class SubsetProduct:
    """
    Find the number of non-empty subsets whose product of elements is less than or equal to a given integer K.
    See https://practice.geeksforgeeks.org/problems/number-of-subsets-with-product-less-than-k/0/
    """

    def count(self, arr, n, k):
        if n == 0:
            return 0
        if n == 1:
            return 1 if arr[0] <= k else 0
        N2 = n // 2
        arr1 = [a for i, a in enumerate(arr) if i < N2 and a <= k]
        arr2 = [a for i, a in enumerate(arr) if i >= N2 and a <= k]
        count = self.count(arr1, len(arr1), k) + self.count(arr2, len(arr2), k)
        prod1 = [1]
        while len(arr1) > 0:
            a1 = arr1.pop()
            prod1 = [*prod1, *[a1 * a for a in prod1 if a1 * a <= k]]
        prod1 = sorted(prod1[1:])
        prod2 = [1]
        while len(arr2) > 0:
            a2 = arr2.pop()
            prod2 = [*prod2, *[a2 * a for a in prod2 if a2 * a <= k]]
        prod2 = sorted(prod2[1:])
        for i in range(0, len(prod1)):
            count += bisect(prod2, (k // prod1[i]))  # TODO: fix
        return count
