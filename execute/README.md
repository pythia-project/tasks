# Code executor

The _code executor_ tasks can be used to execute a given code and retrieve the result it produced on the standard output.

## Specification

### Input

The code to execute.

### Output

A JSON object with the following fields:

- **returncode** (_int_) – the return code of the executed code
- **stdout** (_string_) – the content of the standard output, if any (optional)
- **stderr** (_string_) – the content of the standard error, if any (optional)

## Example

The following example is a Python program printing `Hello World!` on the standard output:

### Input

    print('Hello World!', end='')

### Output

    {
      "returncode": 0,
      "stdout": "Hello World!",
      "stderr": ""
    }

## Supported languages

- Ada (6.1)
- Algol68 (2.8)
- Bash (4.4)
- C (GCC 6.3)
- C++ (G++ 6.3)
- Go (1.7)
- Java (OpenJDK 8)
- Lua (5.3)
- NodeJS (4.8.2)
- PHP (7.0)
- Prolog (7.2.3)
- Python (3.5.3-1)
- Rexx (3.6)
- Rust (1.24.1)
- Tcl (8.6.6)
