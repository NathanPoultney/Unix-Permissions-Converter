#!/usr/bin/env python3
"""
Example usage of the permissions_converter module.
"""

from permissions_converter import int_to_permissions, permissions_to_int

# Example usage
if __name__ == "__main__":
    # Example 1: Integer to permission string
    perm_num = 755
    perm_str = int_to_permissions(perm_num)
    print(f"{perm_num} -> {perm_str}")
    
    # Example 2: Permission string to integer
    perm_str = "rwxr-xr-x"
    perm_num = permissions_to_int(perm_str)
    print(f"{perm_str} -> {perm_num}")
    
    # Additional examples
    examples = [644, 777, 600, 444]
    for ex in examples:
        perm_str = int_to_permissions(ex)
        print(f"{ex} -> {perm_str} -> {permissions_to_int(perm_str)}")
    
    print("\nHandling invalid inputs:")
    
    # Invalid permission number
    invalid_num = 888
    result = int_to_permissions(invalid_num)
    print(f"Invalid number {invalid_num} -> {result}")
    
    # Invalid permission strings
    invalid_strings = [
        "rwa-r--r--", # Contains invalid character
        "rwxrwxrw",   # Too short
        "rwxrwxrwxr", # Too long
        "abcdefghi"   # Invalid characters
    ]
    
    for inv_str in invalid_strings:
        result = permissions_to_int(inv_str)
        print(f"Invalid string '{inv_str}' -> {result}")