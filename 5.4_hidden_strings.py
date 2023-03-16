import re

def read_in_parts(filename, chunk_size=1024):
    with open(filename, 'rb') as f:  # open the file in binary
        while f:
            data = f.read(chunk_size)
            if not data:
                break
            yield data


pattern = rb'[a-z]{5,}!'  # pattern for lowercase letters followed by an exclamation mark

for chunk in read_in_parts('logo.jpg', 4096):
    matches = re.findall(pattern, chunk)  # match the pattern for the part of the file
    for match in matches:
        print(match.decode())  # Convert bytes to string and print
