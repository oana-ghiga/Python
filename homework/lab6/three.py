# Create a Python script that calculates the total size of all files in a directory provided as a command line argument. The script should:
# Use the sys module to read the directory path from the command line.
# Utilize the os module to iterate through all the files in the given directory and its subdirectories.
# Sum up the sizes of all files and display the total size in bytes.
# Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.

import os
import sys

def calculate_total_size(directory):
    total_size = 0
    try:
        if not os.path.isdir(directory):
            print(f"Error: The directory {directory} does not exist.")
            return

        for dirpath, dirnames, filenames in os.walk(directory):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

    except Exception as e:
        print(f"Error: {str(e)}")

    print(f"Total size is {total_size} bytes.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python three.py [directory]")
    else:
        calculate_total_size(sys.argv[1])