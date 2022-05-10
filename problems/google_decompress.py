class GoogleDecompress:
    """
    https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!
    """

    def decompress(self, s: str) -> str:
        accs = [[1, ""]]
        index = 0
        while index < len(s):
            number_str = ""
            while s[index] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                number_str += s[index]
                index += 1
            if number_str != "":
                number = int(number_str)
                accs.append([number, ""])
            elif s[index] == "[":
                pass
            elif s[index] == "]":
                acc = accs.pop()
                accs[-1][1] = accs[-1][1] + acc[0] * acc[1]
            else:  # letter
                accs[-1][1] = accs[-1][1] + s[index]
            index += 1
        return accs[0][1]
