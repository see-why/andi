import os

def get_file_content(working_directory, file_path):
    try:
        # Convert paths to absolute paths for comparison
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

        # Check if target file is outside working directory
        # Ensure the target file is within the working directory
        if os.path.commonpath([working_dir_abs, target_file_abs]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if path exists and is a file
        if not os.path.exists(target_file_abs):
            return f'Error: File not found: "{file_path}"'
        if not os.path.isfile(target_file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file content
        with open(target_file_abs, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if content needs to be truncated
        if len(content) > 10000:
            content = content[:10000] + f'\n[...File "{file_path}" truncated at 10000 characters]'

        return content

    except Exception as e:
        return f'Error: {str(e)}'
