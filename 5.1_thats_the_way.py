import os

folder_path = '/path/to/folder'  # replace with the path to your folder
search_pattern = 'pattern'  # replace with the pattern you want to search for

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file name contains the search pattern
    if search_pattern in filename:
        # If the pattern is found, print the file name
        print(filename)
