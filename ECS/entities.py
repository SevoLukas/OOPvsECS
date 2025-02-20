ENTITIES = set()

_next_entity_id = 0

_names = []
_descriptions = []
_prices = []
_valid = []  # Boolean list to indicate whether an index is currently active


def _expand_storage(new_capacity: int):
    """Internal helper to expand storage to at least new_capacity elements."""
    current_capacity = len(_valid)
    if new_capacity <= current_capacity:
        return  # No need to expand
    # Expand each list to match the new capacity
    _names.extend([""] * (new_capacity - current_capacity))
    _descriptions.extend([""] * (new_capacity - current_capacity))
    _prices.extend([0] * (new_capacity - current_capacity))
    _valid.extend([False] * (new_capacity - current_capacity))


def create_product_entity(name: str, description: str, price: int) -> int:
    """
    Creates a new product entity. The ID returned is just an index in the lists.
    """

    # First, see if there's a free slot by checking for an inactive index:
    # We'll do a simple linear scan here, but you could optimize with a free-list.
    for idx, in_use in enumerate(_valid):
        if not in_use:
            # Found a free slot
            _valid[idx] = True
            _names[idx] = name
            _descriptions[idx] = description
            _prices[idx] = price
            return idx


        # If we haven't found a free slot, expand the storage and use the next index
        old_capacity = len(_valid)
        new_capacity = max(1, old_capacity * 2)  # Simple doubling strategy
        _expand_storage(new_capacity)

        # The newly available index is old_capacity
        entity_id = old_capacity
        _valid[entity_id] = True
        _names[entity_id] = name
        _descriptions[entity_id] = description
        _prices[entity_id] = price
        return entity_id


def remove_entity(entity_id: int):
    """
    Marks an entity as inactive, effectively removing it.
    Does not shrink storage to keep it simple.
    """
    if 0 <= entity_id < len(_valid) and _valid[entity_id]:
        _valid[entity_id] = False

def get_product_summary(entity_id: int) -> str:
    """
    Returns a string summary of the product entity’s data.
    """
    if 0 <= entity_id < len(_valid) and _valid[entity_id]:
        return (
        f"Entity {entity_id}:\n"
        f"  Name: {_names[entity_id]}\n"
        f"  Description: {_descriptions[entity_id]}\n"
        f"  Price: {_prices[entity_id]}"
        )
    else:
        return f"Entity {entity_id} not active or out of range."


if __name__ == "main":
    # Example usage
    # Create 3 product entities
    product_a_id = create_product_entity("Widget A", "A high-quality widget", 1299)
    product_b_id = create_product_entity("Widget B", "A budget-friendly widget", 599)
    product_c_id = create_product_entity("Widget C", "A premium widget", 2599)
    print(get_product_summary(product_a_id))
    print(get_product_summary(product_b_id))
    print(get_product_summary(product_c_id))

    # Remove product B
    remove_entity(product_b_id)
    print(get_product_summary(product_b_id))