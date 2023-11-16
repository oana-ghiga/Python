# Write a script using the os module that renames all files in a specified directory to have a sequential number sufix. For example, file1.txt, file2.txt, etc.
# Include error handling for cases like the directory not existing or files that can't be renamed.

import os
import sys

def rename_files(directory):
    try:
        if not os.path.isdir(directory):
            print(f"Error: The directory {directory} does not exist.")
            return

        for count, filename in enumerate(os.listdir(directory)):
            base_name = os.path.splitext(filename)[0]
            new_name = f"{base_name}{count+1}{os.path.splitext(filename)[1]}"

            src = os.path.join(directory, filename)
            dst = os.path.join(directory, new_name)

            try:
                os.rename(src, dst)
            except Exception as e:
                print(f"Error renaming file {filename}: {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python two.py [directory]")
    else:
        rename_files(sys.argv[1])
