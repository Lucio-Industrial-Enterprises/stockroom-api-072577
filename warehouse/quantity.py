"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a non-negative quantity, raising ValueError for invalid input."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    return quantity
