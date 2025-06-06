import os

def delete_file(working_directory, file_path):
    try:
        # Convert paths to absolute paths for comparison
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

        # Check if target file is outside working directory
        if not target_file_abs.startswith(working_dir_abs):
            return f'Error: Cannot delete "{file_path}" as it is outside the permitted working directory'

        # Check if file exists
        if not os.path.exists(target_file_abs):
            return f'Error: File not found: "{file_path}"'

        # Delete the file
        os.remove(target_file_abs)

        return f'Successfully deleted "{file_path}"'

    except Exception as e:
        return f'Error: {str(e)}' 