#!/usr/bin/env python3
"""
Tests for the permissions_converter module.

This test file contains pytest-based tests for both int_to_permissions and
permissions_to_int functions, with various test cases including valid
and invalid inputs.
"""

import pytest
from permissions_converter import int_to_permissions, permissions_to_int


class TestIntToPermissions:
    """Tests for the int_to_permissions function."""
    
    def test_valid_permissions(self):
        """Test valid permission numbers."""
        test_cases = [
            (0, "---------"),
            (1, "--------x"),
            (7, "------rwx"),
            (70, "---rwx---"),
            (700, "rwx------"),
            (755, "rwxr-xr-x"),
            (644, "rw-r--r--"),
            (777, "rwxrwxrwx"),
            (600, "rw-------"),
            (444, "r--r--r--"),
        ]
        
        for num, expected in test_cases:
            assert int_to_permissions(num) == expected
    
    def test_invalid_permissions(self):
        """Test invalid permission numbers."""
        invalid_cases = [-1, 778, 800, 900, 1000]
        
        for num in invalid_cases:
            assert int_to_permissions(num) == "Invalid permission number"


class TestPermissionsToInt:
    """Tests for the permissions_to_int function."""
    
    def test_valid_permission_strings(self):
        """Test valid permission strings."""
        test_cases = [
            ("---------", 0),
            ("--------x", 1),
            ("------rwx", 7),
            ("---rwx---", 70),
            ("rwx------", 700),
            ("rwxr-xr-x", 755),
            ("rw-r--r--", 644),
            ("rwxrwxrwx", 777),
            ("rw-------", 600),
            ("r--r--r--", 444),
        ]
        
        for perm_str, expected in test_cases:
            assert permissions_to_int(perm_str) == expected
    
    def test_invalid_permission_strings(self):
        """Test invalid permission strings."""
        invalid_cases = [
            "",                  # Empty string
            "rwx",               # Too short
            "rwxrwxrwxrwx",      # Too long
            "rwxrwxrw",          # Missing one character
            "abcdefghi",         # Invalid characters
            "rw-r--r-a",         # Contains an invalid character
            "rwa-r--r--",        # Invalid 'a' character where 'x' or '-' expected
        ]
        
        for perm_str in invalid_cases:
            assert permissions_to_int(perm_str) == "Invalid permission string"


class TestRoundTrip:
    """Test round-trip conversions."""
    
    def test_int_to_permissions_to_int(self):
        """Test converting from int to string and back to int."""
        test_cases = [0, 1, 7, 70, 644, 700, 755, 777]
        
        for num in test_cases:
            perm_str = int_to_permissions(num)
            assert permissions_to_int(perm_str) == num
            
    def test_permissions_to_int_to_permissions(self):
        """Test converting from string to int and back to string."""
        test_cases = [
            "---------",
            "--------x",
            "------rwx",
            "---rwx---",
            "rwx------",
            "rwxr-xr-x",
            "rw-r--r--",
            "rwxrwxrwx",
        ]
        
        for perm_str in test_cases:
            num = permissions_to_int(perm_str)
            assert int_to_permissions(num) == perm_str


if __name__ == "__main__":
    pytest.main(["-v", __file__])