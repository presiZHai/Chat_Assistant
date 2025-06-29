import os

def create_project_structure(base_path="."):
    """
    Creates the specified project structure (files) within the current working directory.
    Existing files with the same name will be ignored to prevent accidental overwrites.

    Args:
        base_path (str): The path to the directory where files should be created.
                         Defaults to "." (the current directory).
    """
    
    # Define the structure: only files in the base directory
    # No subdirectories are explicitly defined in this structure, as per the image
    structure = {
        ".": [ # Represents the base directory itself (the current directory)
            ".env",
            ".gitignore",
            "app.py",
            "functions.py",
            "requirements.txt",
            "README.md"
        ]
    }

    print(f"Attempting to create files in: {os.path.abspath(base_path)}\n")

    # The base directory (Sage) is assumed to already exist, as the user is in it.
    # Therefore, no os.makedirs for the base_path is needed here.
    # If this script were to be run from outside the target directory,
    # and base_path was, for example, "my_project_name", then os.makedirs
    # would be necessary to create "my_project_name" first.

    for folder, files in structure.items():
        # current_path will be the base_path (e.g., ".") if folder is "."
        # If there were subdirectories (e.g., "src"), current_path would be "./src"
        current_path = os.path.join(base_path, folder)
        
        # This check is more relevant if 'structure' contained subdirectories like 'src'
        # For this specific structure, 'folder' will always be '.', so this block is not strictly
        # necessary for creating subdirectories, but it's harmless due to exist_ok=True.
        if folder != ".":
            os.makedirs(current_path, exist_ok=True)
            print(f"Created directory: {current_path}/ (if it didn't exist)")

        for file_name in files:
            file_path = os.path.join(current_path, file_name)
            if not os.path.exists(file_path):
                try:
                    with open(file_path, 'w') as f:
                        pass  # Create an empty file
                    print(f"Created file: {file_path}")
                except IOError as e:
                    print(f"Error creating file {file_path}: {e}")
            else:
                print(f"Skipped existing file: {file_path}")
    
    print("\nProject structure creation process completed.")

if __name__ == "__main__":
    # When running this script from within the 'Sage' directory,
    # the default base_path="." will correctly place files directly inside 'Sage'.
    create_project_structure()
# This script creates a predefined project structure with specific files.
# It checks for existing files to avoid overwriting them.
# The structure is defined in a dictionary, where the key is the folder path
# and the value is a list of file names to create in that folder.
# The script prints messages indicating the creation of directories and files,
# and it handles any errors that may occur during file creation.
# The script is designed to be run from the command line, and it will create files
# in the current working directory unless a different base path is specified.