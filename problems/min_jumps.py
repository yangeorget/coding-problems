class MinJumps:
    """
    See https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
    """
    def min_jumps(self, arr, n):
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        max_reachable_index = arr[0]
        remaining_steps = arr[0]
        current_jump = 1
        for index in range(1, n - 1):
            max_reachable_index = max(max_reachable_index, index + arr[index])
            if index == max_reachable_index:
                return -1
            remaining_steps -= 1
            if remaining_steps == 0:
                current_jump += 1
                remaining_steps = max_reachable_index - index
        return current_jump
