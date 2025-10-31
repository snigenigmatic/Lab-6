from hypothesis import given, strategies as st
from processor import sanitize_string, parse_int_list, reverse_words

@given(st.text() | st.none())
def test_sanitize_string_no_crash(s):
    # To-Do:Using try and except complete this function.
    pass
    
@given(st.text() | st.none())
def test_parse_int_list_safe(s):
    # To-Do:Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_reverse_words_safe(s):
    # To-Do:Using try and except complete this function.
    pass