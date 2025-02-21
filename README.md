
# Match Case Statements in Python

This repository contains examples and explanations of Python's `match-case` statements introduced in Python 3.10. These examples aim to demonstrate various use cases and practical applications of pattern matching.

## Features

- Simple examples to understand the syntax.
- Real-world scenarios showcasing the power of match-case statements.
- Examples with pattern matching in lists, dictionaries, and classes.

## Prerequisites

To run the examples in this repository, ensure you have Python 3.10 or later installed on your system. 

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/shreyash0019/match-case-statements-python.git
    ```
2. Navigate to the repository folder:
    ```bash
    cd match-case-statements-python
    ```
3. Run the examples:
    ```bash
    python <example_file>.py
    ```

Replace `<example_file>` with the name of the desired Python file.

## Match-Case Overview

`match-case` statements in Python provide a way to perform pattern matching, which is particularly useful for complex conditions and control flows. Here's a basic example:

```python
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(http_status(404))  # Output: Not Found
```

## Contributions

Contributions are welcome! If you have examples or improvements to add, feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Developed by Shreyash Ingle. Connect with me on [LinkedIn](https://www.linkedin.com/in/shreyash-ingle-).
