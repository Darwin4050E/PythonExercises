"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    result = {}
    for item in items:
        if item not in result:
            result[item] = items.count(item)
    return result


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    result = create_inventory(items)
    for key in inventory:
        result[key] = result.get(key, 0) + inventory[key]
    return result


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    dict_items = {}
    result = inventory
    for item in items:
        if item not in dict_items:
            dict_items[item] = items.count(item)
    for key in result:
        operation = result[key] - dict_items.get(key, 0)
        result[key] = operation if operation >= 0 else 0
    return result


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    result = inventory
    result.pop(item, "unknow")
    return result


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    result = []
    for key in inventory:
        if inventory[key]:
            result.append((key, inventory[key]))
    return result

