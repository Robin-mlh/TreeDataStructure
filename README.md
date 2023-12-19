# TreeDataStructure
Simple Python functions for building and interacting with a data structure based on the directories tree. 

## Key Features:

**Addition of Values:** The add_item function allows users to add values to specific directory paths, creating a nested dictionary structure. Values are stored in lists under a specified key.

**Retrieval of Elements:** The get_items function facilitates the retrieval of elements located at a specified path within the directory structure, providing either a dictionary at the path level or a list of elements.

**Update and delete:** The update_item function is used to modify or delete a value or directory.

## Examples:

```
add_item('laptops/thinkpad', 't490')

add_item('laptops/thinkpad', ['t480', 't470'])

add_item('laptops/acer', 'a5 2022')

add_item('laptops/acer/a7', '2023')

print("/laptops :", get_items('laptops'))

/laptops : {'thinkpad': {'values': ['t490', 't480', 't470']}, 'values': ['L450'], 'acer': {'values': ['a5 2022'], 'a7': {'values': ['2023']}}}

print("/laptops/thinkpad/values :", get_items("laptops/thinkpad/values"))

/laptops/thinkpad/values : ['t490', 't480', 't470']

update_item("laptops/thinkpad/values", "t490", "t490s")
