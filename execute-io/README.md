# Input-Output task executor

The _input-output task executor_ tasks can be used to execute a given code that receives an input on the standard input and to check that it produces the correct result on the standard output.


## Specification

### Input

A JSON object with the following fields:

- **tid** (_string_) – an identifier for this task execution
- **header** (_string_) – the header of the code to execute (optional)
- **code** (_string_) – the body of the code to execute
- **inputs** (_string[]_) – the list of inputs to test the code with
- **outputs** (_string[]_) – the list of expected results for each input test
- **mirror** (_boolean_) – whether the inputs and outputs are sent back in the output (optional, default: false)

### Output

A JSON object with the following fields:

- **tid** (_string_) – the identifier for this task execution
- **status** (_string_) – the status of execution (error, failed or success)
- **message** (_string_) – an error message (optional)
- **inputs** (_string[]_) – the list of inputs to test the code with (optional)
- **outputs** (_object_)
  - **expected** (_string_) – the list of expected results for each input test (optional)
  - **actual** (_string_) – the outputs produced by the executed code
- **valid** (_boolean[]_) – whether each output produced by the executed code is equal to the expected output

The value of the **tid**, **inputs** and **outputs.expected** fields are just copied from the input. The last two are only present if the **mirror** field is set to _true_ in the input.

## Example

The following example is a Python input-output task for which a correct solution must print on the standard output the exact content read on the standard input:

### Input

    {
      "tid": "execute-io-python-test",
      "header": "import sys",
      "code": "print(sys.stdin.read(), end='')",
      "inputs": ["1", "HELLO"],
      "outputs": ["1", "HELLO"]
    }

### Output

    {
      "tid": "execute-io-python-test",
      "status": "success",
      "outputs": {
        "actual": ["1", "HELLO"]
      },
      "valid": [true, true]
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
