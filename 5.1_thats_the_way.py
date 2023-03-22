import os
import re


def that_the_way(folder_path):
    """@:param folder_path: path to the folder to search in

    """
    # Loop over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file name contains the search pattern
        if re.match(search_pattern, filename): # If the pattern is found, print the file name
            print(filename)


folder_path = 'images'  # replace with the path to your folder
search_pattern = r'^deep.*'
that_the_way(folder_path)

