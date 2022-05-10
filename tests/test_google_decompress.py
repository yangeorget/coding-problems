from problems.google_decompress import GoogleDecompress


class TestGoogleDecompress:
    def test_decompress(self) -> None:
        assert GoogleDecompress().decompress("3[abc]4[ab]c") == "abcabcabcababababc"
        assert GoogleDecompress().decompress("10[a]") == "aaaaaaaaaa"
        assert GoogleDecompress().decompress("2[3[a]b]") == "aaabaaab"
