"""Function to help determine transposed text of a given text.
"""

def transpose(text):
    """Determine transposed text of a given text.

    :param text: - text to be transposed.
    :return: str - transposed text.
    """
    lines = text.split("\n")
    max_len = max(len(line) for line in lines) if text else 0
    result = []
    for c in range(max_len):
        column_chars = []
        for r in range(len(lines)):
            if c < len(lines[r]):
                column_chars.append(lines[r][c])
            else:
                if any(c < len(lines[future_r]) for future_r in range(r + 1, len(lines))):
                    column_chars.append(" ")
        result.append("".join(column_chars))
    return "\n".join(result)