"""
Cstigen's code
"""


def anonymize(obj, marker):
    """
    Recursively removes object elements with marker, keeping dict keys and
    overall structure.

    Used to anonymize sensitive data.

    :param obj: Object to anonymize
    :param marker: Object to set in sensitive locations

    :return: Copy of object with the same structure
    """

    if isinstance(obj, dict):
        return {k: anonymize(v, marker) for (k, v) in obj.items()}

    if isinstance(obj, list):
        return list(anonymize(e, marker) for e in obj)

    if isinstance(obj, tuple):
        return tuple(anonymize(e, marker) for e in obj)

    return marker


def anonymized_format(obj, marker=None):
    """
    Returns an anonymized string representation of the object with sensitive
    data marked.

    :param obj: Object to anonymize
    :param marker: Replaces sensitive spots in the object. Its repr will be
                   used for printing.

    :return: String
    """
    if marker is None:
        marker = "?"

    obj = anonymize(obj, marker)

    string = repr(obj)
    string = string.replace(": %s" % repr(marker), "")
    string = string.replace(repr(marker), marker)
    return string


print(anonymized_format({"a": 2, "b": [9, 8], "c": {"x": [(1,2), 7]}}))  # {'c': {'x': [(?, ?), ?]}, 'a', 'b': [?, ?]}
