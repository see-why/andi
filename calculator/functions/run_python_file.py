import os
import subprocess
import sys

def run_python_file(working_directory, file_path):
    try:
        # Convert paths to absolute paths for comparison
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

        # Check if target file is outside working directory
        if not target_file_abs.startswith(working_dir_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if file exists
        if not os.path.exists(target_file_abs):
            return f'Error: File "{file_path}" not found.'

        # Check if file is a Python file
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        # Run the Python file
        result = subprocess.run(
            [sys.executable, target_file_abs],
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        # Build output string
        output_parts = []
        
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)

    except subprocess.TimeoutExpired:
        return f'Error: Process timed out after 30 seconds'
    except Exception as e:
        return f'Error: executing python file {str(e)}'
        