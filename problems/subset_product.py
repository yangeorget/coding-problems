from bisect import bisect


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
        left = arr[: n // 2]
        right = arr[n // 2 :]
        count = self.count(left, len(left), k) + self.count(right, len(right), k)
        left_products = self.products(left, k)
        right_products = self.products(right, k)
        for p in left_products:
            count += bisect(right_products, (k // p))  # TODO: fix
        return count
