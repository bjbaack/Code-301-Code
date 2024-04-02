#!/usr/bin/python3

#!/usr/bin/env python3

# Import libraries
import os
import subprocess

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
    
    # Open .txt file with LibreOffice Writer
    subprocess.run(["libreoffice", "--writer", "directory_info.txt"])

# Main
if __name__ == "__main__":
    generate_directory_info(user_path)

# Stretch Goal: Function to prepare a test directory
def prepare_test_directory(base_name):
    """
    Creates a directory and sub-directories as per user input.
    """
    base_path = os.path.join(os.getcwd(), base_name)
    os.makedirs(base_path, exist_ok=True)
    for i in range(1, 4):
        os.makedirs(os.path.join(base_path, f"{base_name}_{i:02}"), exist_ok=True)

# Uncomment the line below to use the prepare_test_directory function
# prepare_test_directory(input("Enter a name for the base test directory: "))
