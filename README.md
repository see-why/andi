# Andi modifies a calculator

A Python-based LLM project with a focus on file changes and running python scripts.

## Project Structure

```
calculator/
├── functions/
│   ├── get_file_content.py
│   ├── write_file.py
│   ├── delete_file.py
│   └── run_python_file.py
├── pkg/
│   └── calculator.py
├── main.py
└── tests.py
```

## Function Documentation

### get_file_content(working_directory, file_path)
Reads and returns the contents of a file within the working directory.

**Parameters:**
- `working_directory` (str): The base directory for file operations
- `file_path` (str): Path to the file relative to working_directory

**Returns:**
- File contents as string
- Error message if file is outside working directory or doesn't exist
- Truncates files longer than 10000 characters

**Example:**
```python
content = get_file_content("calculator", "main.py")
```

### write_file(working_directory, file_path, content)
Writes content to a file within the working directory.

**Parameters:**
- `working_directory` (str): The base directory for file operations
- `file_path` (str): Path to the file relative to working_directory
- `content` (str): Content to write to the file

**Returns:**
- Success message with character count
- Error message if file is outside working directory

**Example:**
```python
result = write_file("calculator", "output.txt", "Hello, World!")
```

### delete_file(working_directory, file_path)
Deletes a file within the working directory.

**Parameters:**
- `working_directory` (str): The base directory for file operations
- `file_path` (str): Path to the file relative to working_directory

**Returns:**
- Success message
- Error message if file is outside working directory or doesn't exist

**Example:**
```python
result = delete_file("calculator", "output.txt")
```

### run_python_file(working_directory, file_path)
Executes a Python file within the working directory.

**Parameters:**
- `working_directory` (str): The base directory for file operations
- `file_path` (str): Path to the Python file relative to working_directory

**Returns:**
- Combined stdout and stderr output
- Process exit code if non-zero
- Error message if file is outside working directory, doesn't exist, or isn't a Python file
- Timeout after 30 seconds

**Example:**
```python
result = run_python_file("calculator", "main.py")
```

## Security Features

All functions include the following security measures:
- Path normalization to prevent path traversal attacks
- Strict checking of file boundaries
- File existence verification
- Comprehensive error handling
- Clear error messages

## Running Tests

To run the test suite:
```bash
python3 calculator/tests.py
```

The test suite includes:
- File content reading tests
- File writing tests
- File deletion tests
- Python file execution tests
- Error case handling tests

## Error Handling

All functions return error messages as strings instead of raising exceptions. This allows for graceful error handling and clear feedback. Error messages are always prefixed with "Error:" for easy identification.

## File Size Limits

- `get_file_content`: Truncates files longer than 10000 characters
- `run_python_file`: Times out after 30 seconds of execution

## Working Directory

All file operations are restricted to the specified working directory. Attempts to access files outside this directory will result in error messages.
