import os
import subprocess
import sys


def execute_python_files():
    """
    This function loops through all Python files in the current directory (except for files starting with "main")
    and executes them using the os.system() method.
    """

    # Get the current directory
    current_dir = os.getcwd()
    python_path = sys.executable

    # Add the current directory to the system path
    sys.path.append(current_dir)

    # Loop through all files in the directory
    for filename in os.listdir(current_dir):
        # Check if the file is a Python file and not the main file
        if filename.endswith('.py') and not filename.startswith('main'):
            # Execute the Python file
            print("Output for", filename, "is:")
            subprocess.run([python_path, filename])
            print("-" * 50)


if __name__ == '__main__':
    # Call the main function when the script is run
    execute_python_files()
