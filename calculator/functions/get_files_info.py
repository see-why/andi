import os
from pathlib import Path

def get_files_info(working_directory, directory=None):
    try:
        # Convert paths to absolute paths for comparison
        working_dir_abs = os.path.abspath(working_directory)
        if directory:
            target_dir_abs = os.path.abspath(os.path.join(working_dir_abs, directory))
        else:
            target_dir_abs = working_dir_abs

        # Check if target directory is outside working directory
        if os.path.commonpath([working_dir_abs, target_dir_abs]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if path exists and is a directory
        if not os.path.exists(target_dir_abs):
            return f'Error: "{directory}" does not exist'
        if not os.path.isdir(target_dir_abs):
            return f'Error: "{directory}" is not a directory'

        # Build the directory listing
        result = []
        for item in sorted(os.listdir(target_dir_abs)):
            item_path = os.path.join(target_dir_abs, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            result.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')

        return '\n'.join(result)

    except Exception as e:
        return f'Error: {str(e)}'
  
  