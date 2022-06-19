class BinarySearch:
    def binarysearch(self, arr, n, k):
        return self._binarysearch(arr, 0, n, k)

    def _binarysearch(self, arr, low, hi, k):
        if low == hi:
            return -1
        if low + 1 == hi:
            return low if arr[low] == k else -1
        left = self._binarysearch(arr, low, (low + hi) // 2, k)
        if left != -1:
            return left
        right = self._binarysearch(arr, (low + hi) // 2, hi, k)
        return right