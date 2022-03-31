class Boggle:
    """
    See https://practice.geeksforgeeks.org/problems/word-boggle4143/1/
    """
    def word_boggle(self, board, dictionary):
        positions = self.compute_positions(board)
        return sorted(
            [word for word in dictionary if self.is_feasible(board, positions, word)]
        )

    def compute_positions(self, board):
        positions = {}
        for i, line in enumerate(board):
            for j, letter in enumerate(line):
                if letter not in positions:
                    positions[letter] = []
                positions[letter].append((i, j))
        return positions

    def is_feasible(self, board, positions, word):
        if word[0] in positions:
            for i, j in positions[word[0]]:
                if self._is_feasible(board, i, j, word, []):
                    return True
        return False

    def _is_feasible(self, board, i, j, word, path):
        if len(path) == len(word):
            return True
        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or (i, j) in path
            or board[i][j] != word[len(path)]
        ):
            return False
        return (
            self._is_feasible(board, i - 1, j - 1, word, [*path, (i, j)])
            or self._is_feasible(board, i - 1, j, word, [*path, (i, j)])
            or self._is_feasible(board, i - 1, j + 1, word, [*path, (i, j)])
            or self._is_feasible(board, i, j - 1, word, [*path, (i, j)])
            or self._is_feasible(board, i, j + 1, word, [*path, (i, j)])
            or self._is_feasible(board, i + 1, j - 1, word, [*path, (i, j)])
            or self._is_feasible(board, i + 1, j, word, [*path, (i, j)])
            or self._is_feasible(board, i + 1, j + 1, word, [*path, (i, j)])
        )
