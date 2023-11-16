# Write a Python script that counts the number of files with each extension in a given directory. The script should:
# Accept a directory path as a command line argument (using sys.argv).
# Use the os module to list all files in the directory.
# Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
# Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.

import os
import sys

def count_files_by_extension(directory):
    try:
        if not os.path.isdir(directory):
            print(f"Error: The directory {directory} does not exist.")
            return

        ext_counter = {}

        for root, dirs, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext == '':
                    ext = 'No extension'
                if ext in ext_counter:
                    ext_counter[ext] += 1
                else:
                    ext_counter[ext] = 1

        for ext, count in ext_counter.items():
            print(f"{ext}: {count}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [directory]")
    else:
        count_files_by_extension(sys.argv[1])
