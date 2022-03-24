from problems.parentheses import Parentheses


class TestParentheses:
    def test_max_length(self) -> None:
        assert Parentheses().max_length("(()())") == 6
        assert Parentheses().max_length("()") == 2
        assert Parentheses().max_length("") == 0
        assert Parentheses().max_length(")(") == 0
        assert Parentheses().max_length(")()(") == 2
        assert Parentheses().max_length("()()") == 4
        assert Parentheses().max_length(")()()") == 4
        assert Parentheses().max_length(")())()") == 2
        assert Parentheses().max_length(")()())") == 4
        assert Parentheses().max_length(")(()()") == 4
        assert Parentheses().max_length(")()(()") == 2
        assert Parentheses().max_length(")()()(") == 4
        assert Parentheses().max_length("()(())") == 6
        assert Parentheses().max_length("()(()())") == 8
        assert Parentheses().max_length(")()(()())(") == 8
