import re


def read_in_chunks(f, chunk_size):
    while data := f.read(chunk_size):
        yield data


pattern = rb'[a-z]{5,}!'  # pattern for lowercase letters followed by an exclamation mark

with open('logo.jpg', 'rb') as f:  # open the file in binary
    for chunk in read_in_chunks(f, 1024):
        matches = re.findall(pattern, chunk)  # match the pattern for the part of the file
        for match in matches:
            print(match.decode())  # Convert bytes to string and print
