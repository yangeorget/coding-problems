class SubsetProduct:
    """
    Find the number of non-empty subsets whose product of elements is less than or equal to a given integer K.
    See https://practice.geeksforgeeks.org/problems/number-of-subsets-with-product-less-than-k/0/
    """

    def products(self, arr, k):
        products = [1]
        for x in arr:
            products.extend([x * y for y in products if x * y <= k])
        return sorted(products[1:])

    def count(self, arr, n, k):
        arr = [a for a in arr if a <= k]
        if n <= 1:
            return n
        n2 = n // 2
        count = self.count(arr[:n2], len(arr[:n2]), k) + self.count(arr[n2:], len(arr[n2:]), k)
        products = self.products(arr[n2:], k)
        for x in self.products(arr[:n2], k):
            count += 1 + self.max_index(lambda y: x * y <= k, products, 0, len(products))
        return count

    def max_index(self, f, arr, min, max):
        """
        Returns the maximal index i such that i in [min, max[ and f(arr[i]).
        :param f: a boolean function
        :param arr: an array
        :param min: a minimal bound (included)
        :param max: a maximal bound (excluded)
        :return: an index
        """
        if min + 1 == max:
            return min if f(arr[min]) else -1
        mid = (min + max) // 2
        return self.max_index(f, arr, mid, max) if f(arr[mid]) else self.max_index(f, arr, min, mid)

