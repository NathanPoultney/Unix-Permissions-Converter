#!/usr/bin/env python3
"""
Unix File Permissions Converter

This module provides functions to convert between Unix file permissions in
octal notation (like 755) and symbolic notation (like rwxr-xr-x).
"""

def int_to_permissions(num):
    """Convert integer permission (e.g. 755) to string format (e.g. rwxr-xr-x)"""
    if not isinstance(num, int) or not 0 <= num <= 777:
        return "Invalid permission number"
    
    # Convert to binary, remove '0b' prefix, and ensure it's 9 bits
    binary = bin(int(str(num), 8))[2:].zfill(9)
    
    # Map bits to permission symbols
    symbols = ''
    for bit in binary:
        symbols += 'rwx'[len(symbols) % 3] if bit == '1' else '-'
    
    return symbols

def permissions_to_int(perm_string):
    """Convert string permission (e.g. rwxr-xr-x) to integer format (e.g. 755)"""
    if not isinstance(perm_string, str) or len(perm_string) != 9:
        return "Invalid permission string"
    
    # Check if the string follows valid permission patterns
    for i in range(0, 9):
        char = perm_string[i]
        if i % 3 == 0 and char not in ['r', '-']:  # Position 0/3/6: read permission
            return "Invalid permission string"
        elif i % 3 == 1 and char not in ['w', '-']:  # Position 1/4/7: write permission
            return "Invalid permission string"
        elif i % 3 == 2 and char not in ['x', '-']:  # Position 2/5/8: execute permission
            return "Invalid permission string"
    
    # Convert permission symbols to binary
    binary = ''
    for char in perm_string:
        if char in 'rwx':
            binary += '1'
        elif char == '-':
            binary += '0'
        else:
            return "Invalid permission string"  # Redundant but kept for safety
    
    # Convert binary to octal
    octal = ''
    for i in range(0, 9, 3):
        octal += str(int(binary[i:i+3], 2))
    
    return int(octal)