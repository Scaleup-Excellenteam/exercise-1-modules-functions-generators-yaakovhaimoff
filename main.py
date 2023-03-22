import os

# Get the current directory
current_dir = os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(current_dir):
    # Check if the file is a Python file
    if filename.endswith('.py') and not filename.startswith('main'):
        # Run the Python file
        print("out put for", filename, "is:")
        os.system(f'python {filename}')
        print("-" * 50)
