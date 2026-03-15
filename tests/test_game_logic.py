from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- parse_guess tests ---

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_decimal_rejected():
    ok, value, err = parse_guess("3.14")
    assert ok is False
    assert value is None

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_below_range():
    ok, value, err = parse_guess("0", low=1, high=100)
    assert ok is False
    assert value is None

def test_parse_above_range():
    ok, value, err = parse_guess("101", low=1, high=100)
    assert ok is False
    assert value is None
