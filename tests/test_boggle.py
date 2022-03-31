from problems.boggle import Boggle


class TestBoggle:
    def test_positions(self):
        assert {
            "A": [(0, 1), (1, 0)],
            "C": [(0, 0)],
            "D": [(1, 2)],
            "E": [(2, 2)],
            "I": [(2, 1)],
            "N": [(1, 1)],
            "P": [(0, 2)],
            "T": [(2, 0)],
        } == Boggle().compute_positions(
            [
                ["C", "A", "P"],
                ["A", "N", "D"],
                ["T", "I", "E"],
            ]
        )

    def test_word_boggle_1(self):
        assert ["CAT"] == Boggle().word_boggle(
            [
                ["C", "A", "P"],
                ["A", "N", "D"],
                ["T", "I", "E"],
            ],
            ["CAT"],
        )

    def test_word_boggle_2(self):
        assert ["GEEKS", "QUIZ"] == Boggle().word_boggle(
            [
                ["G", "I", "Z"],
                ["U", "E", "K"],
                ["Q", "S", "E"],
            ],
            ["GEEKS", "FOR", "QUIZ", "GO"],
        )

    def test_word_boggle_3(self):
        assert ["bcd", "db"] == Boggle().word_boggle(
            [["d", "d"], ["b", "f"], ["e", "c"], ["b", "c"], ["d", "c"]],
            ["bcd", "db"],
        )

    def test_word_boggle_4(self):
        assert ["df", "e", "fd"] == Boggle().word_boggle(
            [
                ["f", "f"],
                ["d", "e"],
                ["f", "b"],
                ["b", "e"],
            ],
            ["df", "dec", "dfd", "fd", "ded", "e"],
        )

    def test_word_boggle_5(self):
        assert [
            "syyylyjqzdwjlxywmfbpfuofwjunttsikvmrlwpncskvye"
        ] == Boggle().word_boggle(
            [
                ["b", "v", "h", "i", "o", "f", "q", "j", "y", "y"],
                ["t", "y", "v", "d", "x", "j", "z", "d", "y", "l"],
                ["v", "e", "k", "n", "w", "l", "i", "w", "y", "s"],
                ["i", "f", "s", "c", "p", "m", "r", "j", "l", "x"],
                ["l", "d", "h", "n", "u", "j", "v", "m", "w", "y"],
                ["n", "c", "d", "t", "t", "w", "k", "f", "b", "p"],
                ["c", "l", "f", "g", "s", "i", "f", "o", "u", "f"],
            ],
            [
                "uobfpyljwyydyylsxwfkvmrjuttgfdhdclnlivefscnpmizjqjxdnwlufuhydujxj",
                "qzjliwdylxywbufpte",
                "syyylyjqzdwjlxywmfbpfuofwjunttsikvmrlwpncskvye",
                "pmljfzdwysxypfbwljrirvidinsfmnrpkarwvspxwqbpwtplnyhxawqwnxjaqaopohlw",
                "iwdyyyylsxypfufmbokwisgtdflchncpmjrjlwmxog",
                "xlwbfmjrvkwisgtuncpjmiwdjyylsyyvnskvdgyoxrwucbknfniwmyojctdxqnidxlqky",
            ],
        )
