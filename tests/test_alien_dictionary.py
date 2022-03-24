from problems.alien_dictionary import AlienDictionary


class TestAlienDictionary:
    def test_get_edge(self) -> None:
        assert not AlienDictionary().get_edge("abc", "abc")
        assert AlienDictionary().get_edge("abd", "abc") == (3, 2)
        assert AlienDictionary().get_edge("baa", "abcd") == (1, 0)

    def test_find_order1(self) -> None:
        assert AlienDictionary().find_order([], 0, 8) == "abcdefgh"
        assert AlienDictionary().find_order(["bdcace"], 1, 8) == "abcdefgh"

    def test_find_order2(self) -> None:
        assert AlienDictionary().find_order(["baa", "abcd", "abca", "cab", "cad"], 5, 4) == "bdac"
