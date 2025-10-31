def sanitize_string(data):
    """
    Removes special characters and trims the input.
    Handles None and non-string inputs by converting to string or returning empty string.
    """
    if data is None:
        return ""
    if not isinstance(data, str):
        # convert other types (numbers, objects) to string safely
        try:
            data = str(data)
        except Exception:
            return ""

    data = data.strip()
    for ch in ["!", "@", "#", "$", "%"]:
        data = data.replace(ch, "")
    return data


def parse_int_list(csv_string):
    """
    Parses a CSV string of integers into a list of ints.
    Handles None, empty strings and ignores non-integer tokens.
    """
    if csv_string is None:
        return []
    if not isinstance(csv_string, str):
        try:
            csv_string = str(csv_string)
        except Exception:
            return []

    csv_string = csv_string.strip()
    if csv_string == "":
        return []

    parts = csv_string.split(",")
    ints = []
    for p in parts:
        p = p.strip()
        if p == "":
            continue
        try:
            ints.append(int(p))
        except Exception:
            # skip invalid integer tokens
            continue
    return ints


def reverse_words(sentence):
    """
    Reverses each word in a sentence.
    Handles None and non-string inputs by converting to string or returning empty string.
    """
    if sentence is None:
        return ""
    if not isinstance(sentence, str):
        try:
            sentence = str(sentence)
        except Exception:
            return ""

    words = sentence.split()
    reversed_words = [w[::-1] for w in words]
    return " ".join(reversed_words)


def main():
    print("==== Running sanitize_string ====")
    raw_string = input("Enter a string with special characters (!,@,#,$,%): ")
    clean_string = sanitize_string(raw_string)
    print("Sanitized String:", clean_string)

    print("\n==== Running parse_int_list ====")
    csv_input = input("Enter a CSV of integers (e.g. 1,2,3,4): ")
    int_list = parse_int_list(csv_input)
    print("Parsed Integer List:", int_list)

    print("\n==== Running reverse_words ====")
    sentence_input = input("Enter a sentence without punctuation: ")
    reversed_sentence = reverse_words(sentence_input)
    print("Reversed Words Sentence:", reversed_sentence)


if __name__ == "__main__":
    main()
