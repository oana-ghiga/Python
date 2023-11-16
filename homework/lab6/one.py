#Create a Python script that does the following:
#Takes a directory path and a file extension as command line arguments (use sys.argv).
# Searches for all files with the given extension in the specified directory (use os module).
# For each file found, read its contents and print them.
# Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.
import os
import sys

def read_files(directory, extension):
    try:
        if not os.path.isdir(directory):
            print(f"Error: The directory {directory} does not exist.")
            return

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    try:
                        with open(os.path.join(root, file), 'r') as f:
                            print(f.read())
                    except Exception as e:
                        print(f"Error reading file {file}: {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python one.py [directory] [extension_without_dot]")
    else:
        read_files(sys.argv[1], sys.argv[2])