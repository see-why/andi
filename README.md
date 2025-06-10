# Andi modifies a calculator

A Python-based LLM project with a focus on file changes and running python scripts.

## Project Structure

```
calculator/
├── functions/
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── write_file.py
│   ├── delete_file.py
│   ├── run_python_file.py
│   └── call_function.py
├── calculator/
|   ├── pkg/
│   |    ├── calculator.py
|   |    └── render.py
|   ├── main.py
|   └── tests.py
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

### get_files_info(working_directory, directory_path)
Gets information about files in a directory.

**Parameters:**
- `working_directory` (str): The base directory for file operations
- `directory_path` (str): Path to the directory relative to working_directory

**Returns:**
- Dictionary containing file information (name, size, type, last modified)
- Error message if directory is outside working directory or doesn't exist

**Example:**
```python
info = get_files_info("calculator", "functions")
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

### call_function(working_directory, function_name, **kwargs)
Calls a function by name with the provided arguments.

**Parameters:**
- `working_directory` (str): The base directory for file operations
- `function_name` (str): Name of the function to call
- `**kwargs`: Keyword arguments to pass to the function

**Returns:**
- Function result
- Error message if function doesn't exist or arguments are invalid

**Example:**
```python
result = call_function("calculator", "get_file_content", file_path="main.py")
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
- File information retrieval tests
- File writing tests
- File deletion tests
- Python file execution tests
- Function calling tests
- Error case handling tests

## Error Handling

All functions return error messages as strings instead of raising exceptions. This allows for graceful error handling and clear feedback. Error messages are always prefixed with "Error:" for easy identification.

## File Size Limits

- `get_file_content`: Truncates files longer than 10000 characters
- `run_python_file`: Times out after 30 seconds of execution

## Working Directory

All file operations are restricted to the specified working directory. Attempts to access files outside this directory will result in error messages.
