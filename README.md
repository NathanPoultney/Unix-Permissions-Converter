# Unix File Permissions Converter

A simple Python utility that converts Unix file permissions between integer (octal) notation and symbolic (rwx) notation.

## Features

- Convert from octal permissions (e.g., 755) to symbolic format (e.g., rwxr-xr-x)
- Convert from symbolic permissions (e.g., rwxr-xr-x) to octal format (e.g., 755)
- Error checking for invalid inputs
- Simple command-line examples

## Usage

```python
# Convert octal to symbolic
permission_string = int_to_permissions(755)  # Returns "rwxr-xr-x"

# Convert symbolic to octal
permission_number = permissions_to_int("rwxr-xr-x")  # Returns 755
```

## Example Output

```
755 -> rwxr-xr-x
rwxr-xr-x -> 755
644 -> rw-r--r-- -> 644
777 -> rwxrwxrwx -> 777
600 -> rw------- -> 600
444 -> r--r--r-- -> 444
```

## How It Works

The script demonstrates bitwise operations by:
1. Converting octal to binary representation
2. Processing each bit to determine permissions
3. Grouping bits in sets of 3 to represent user/group/other permissions

## Installation

No external dependencies required. Simply download the script and run it with Python 3:

```bash
git clone https://github.com/NathanPoultney/unix-permissions-converter.git
cd unix-permissions-converter
python3 permissions_converter.py
```

## License

MIT License
