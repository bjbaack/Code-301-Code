#!/usr/bin/python3


# Import libraries
import os

# Read user input into a variable
user_path = input("Please enter a directory path: ")

# Declaration of functions

def generate_directory_info(path):
    """
    Generates and prints directories, sub-directories, and files for a given path.
    Optionally saves the output to a .txt file.
    """
    output = []
    for root, dirs, files in os.walk(path):
        output.append(f"Root: {root}\nDirs: {dirs}\nFiles: {files}\n")
        print(f"Root: {root}")
        print(f"Dirs: {dirs}")
        print(f"Files: {files}")
        print("---")
    
    # Save to .txt file
    with open("directory_info.txt", "w") as f:
        f.write("\n".join(output))
    
    # Open .txt file with LibreOffice Writer (Removed for simplicity)
    # subprocess.run(["libreoffice", "--writer", "directory_info.txt"])

# Main
if __name__ == "__main__":
    generate_directory_info(user_path)
