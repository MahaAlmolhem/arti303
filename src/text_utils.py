"""TODO: describe this module."""


def clean_name(raw):
    """TODO: describe this function."""
    """Clean a name by fixing whitespace and title casing it."""

    # TODO: collapse whitespace, then title-case
    cleaned= " ".join(raw.split())
    return cleaned.title()

