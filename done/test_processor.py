from hypothesis import given, strategies as st
from processor import sanitize_string, parse_int_list, reverse_words


@given(st.text() | st.none())
def test_sanitize_string_no_crash(s):
    # Call sanitize_string with arbitrary text or None and assert it doesn't raise
    try:
        res = sanitize_string(s)
    except Exception as e:
        assert False, f"sanitize_string raised {e!r} for input {s!r}"

    # Basic shape check: result should be a string
    assert isinstance(res, str)


@given(st.text() | st.none())
def test_parse_int_list_safe(s):
    # Call parse_int_list with arbitrary text or None and assert it doesn't raise
    try:
        res = parse_int_list(s)
    except Exception as e:
        assert False, f"parse_int_list raised {e!r} for input {s!r}"

    # Basic shape checks: result should be a list and, if not empty, its items should be ints
    assert isinstance(res, list)
    for item in res:
        assert isinstance(item, int)


@given(st.text() | st.none())
def test_reverse_words_safe(s):
    # Call reverse_words with arbitrary text or None and assert it doesn't raise
    try:
        res = reverse_words(s)
    except Exception as e:
        assert False, f"reverse_words raised {e!r} for input {s!r}"

    # Basic shape check: result should be a string
    assert isinstance(res, str)


def test_parse_int_list_mixed_tokens():
    # Mixed valid ints, empty tokens and non-int tokens should return only the ints
    assert parse_int_list("1, 2, foo, 3,, ,4") == [1, 2, 3, 4]
    assert parse_int_list("") == []


def test_sanitize_string_none_and_strip():
    # None -> empty string, trimming and removal of special chars
    assert sanitize_string(None) == ""
    assert sanitize_string("  hello!@# ") == "hello"


def test_reverse_words_non_string():
    # Non-string inputs are converted to string; numbers reverse their digit order as words
    assert reverse_words(12345) == "54321"
    # punctuation is not removed by reverse_words (sanitize_string is separate)
    assert reverse_words("hi!") == "!ih"
