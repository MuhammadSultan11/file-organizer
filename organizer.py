import os
import shutil

# Set your folder path here
folder_path = r"C:\Users\muham\Downloads"

# File types and their extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Others": []
}


def get_category(filename):
    """Find the category of a file based on its extension"""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    for category, extensions in file_types.items():
        if ext in extensions:
            return category
    return "Others"


def create_folder(folder_name):
    """Create a folder if it does not already exist"""
    path = os.path.join(folder_path, folder_name)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f" Folder created: {folder_name}")


def move_files():
    """Move all files into their organized folders"""

    # Check if the target folder exists
    if not os.path.exists(folder_path):
        print(f"Error: '{folder_path}' folder not found!")
        return

    count = 0  # track how many files were moved

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Move files only, skip folders
        if os.path.isfile(file_path):
            category = get_category(file)
            create_folder(category)

            destination = os.path.join(folder_path, category, file)
            shutil.move(file_path, destination)

            print(f"{file}  →  {category}/")
            count += 1

    print(f"\n Done! {count} files organized successfully.")


#  Run the program
print(" File Organizer Starting...\n")
move_files()
