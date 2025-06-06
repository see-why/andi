import os

def write_file(working_directory, file_path, content):
    try:
        # Convert paths to absolute paths for comparison
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

        # Check if target file is outside working directory
        if not target_file_abs.startswith(working_dir_abs):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(target_file_abs), exist_ok=True)

        # Write content to file
        with open(target_file_abs, 'w', encoding='utf-8') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {str(e)}' 