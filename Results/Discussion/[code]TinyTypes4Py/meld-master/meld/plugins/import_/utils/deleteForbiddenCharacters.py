def deleteForbiddenCharacters(filename: str):
    """
    Removes forbidden characters from filename
    """

    FORBIDDEN_CHARS = {'<', '>', ':', '"', '/', '\\', '|', '?', '*'}

    return ''.join(c for c in filename if c not in FORBIDDEN_CHARS)