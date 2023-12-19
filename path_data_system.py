# Tree-based data structure system with functions
# for adding, modifying, deleting or reading data from a directory path.

data_dict = {}


def add_item(cat_path, value, key="values"):
    """ Add values to the data dictionary to specific location.

    Create a dictionary for each directory.
    Values are stored in a list in value of the 'key' key.
    Exemple: add_item('laptops/thinkpad', 't490', key="values")
    {laptops: {thinkpad: {values: ["t490"]} }}

    cat_path (str) - Path, each directory is separated by '/'.
    value (str or list) - Value(s) to add to cat_path.
                          If it's a list,
                          add all the items in the list.
    key (str) - key to values in a directory.

    Return an error if key is a directory in the path.

    """

    dict_level = data_dict
    path_parts = cat_path.split("/")
    # Browse each category in the cat_path.
    for cat in path_parts:
        if cat == key:
            raise ValueError('The value of key cannot be a directory.')
        # Create a category dictionary if none exists.
        dict_level[cat] = dict_level.get(cat, {})
        dict_level = dict_level[cat]  # Go in this category.

    # Create the list if it doesn't exist and add the value.
    # If value is a list, add all the elements in the list.
    if key in dict_level:
        if isinstance(value, list):
            dict_level[key].extend(value)
        else:
            dict_level[key].append(value)
    else:
        if isinstance(value, list):
            dict_level[key] = value[:]
        else:
            dict_level[key] = [value]


# Test use of the add_item function.
add_item('laptops/thinkpad', 't490')
add_item('laptops', 'L450')
add_item('laptops/thinkpad', ['t480', 't470'])
add_item('laptops/acer', 'a5 2022')
add_item('laptops/acer/a7', '2023')
add_item('desks/ikea', 'small white')


def get_items(path):
    """ Get elements located at path. 
    
    path (str) - The location path for the data to be returned.
    
    return dict_level (dict or list) - Dictionary at path level
                                       or list of elements at path level.
    """
    
    cats = path.split("/")
    dict_level = data_dict
    # If the path argument is not empty, go to the path level.
    if path:
        for c in cats:
            try:
                dict_level = dict_level[c]
            except KeyError:
                raise ValueError(f"The '{c}' directory does not exist.")
    return dict_level

# Test use of the get_items function.
print("/ :", get_items(''))
print("/laptops :", get_items('laptops'))
print("/laptops/thinkpad/values :", get_items("laptops/thinkpad/values"))


def update_item(path, old_value, new_value):
    """ Edit or delete a value or category.

    path (str) - The path to the value to be edited.
    old_value (str) - The value to be edited or deleted.
    new_value (str) - The value to replace the old value.
                      Empty to delete the value.
    """

    return_list = []
    cats = path.split("/")
    dict_level = data_dict
    # If the path argument is not empty, go to the path directory.
    if path:
        for c in cats:
            try:
                dict_level = dict_level[c]
            except KeyError:
                raise ValueError(f"The '{c}' directory does not exist.")
    # Check if the old value exists.
    if not old_value in dict_level:
        raise ValueError(f"'{old_value}' not found at {path}.")
    # If it's a list, change the value found by the index function.
    # If new_value is empty, delete old_value.
    if isinstance(dict_level, list):
        i = dict_level.index(old_value)
        if not new_value:
            del dict_level[i]
        else:
            dict_level[i] = new_value
    else:  # If it's not a list, rename the dictionary key.
        if not new_value:
            del dict_level[old_value]
        else:
            dict_level[new_value] = dict_level.pop(old_value)

print("--- Update Function:")
# Test use of the update_item function.
update_item("laptops/thinkpad/values", "t490", "t490s")
update_item("laptops/thinkpad/values", "t480", "")
print("/laptops/thinkpad/values :", get_items("laptops/thinkpad/values"))
update_item("laptops", "acer", "")
print("/laptops :", get_items("laptops"))