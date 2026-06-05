import os
import shutil

# ✅ Apna path yahan set karo
folder_path = r"C:\Users\muham\Downloads"

# ✅ File types aur unke extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Others": []
}


def get_category(filename):
    """File ka category dhundo extension se"""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    for category, extensions in file_types.items():
        if ext in extensions:
            return category
    return "Others"


def create_folder(folder_name):
    """Folder banao agar exist nahi karta"""
    path = os.path.join(folder_path, folder_name)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"  📂 Folder banaya: {folder_name}")


def move_files():
    """Saari files ko organize karo"""

    # Check karo folder exist karta hai ya nahi
    if not os.path.exists(folder_path):
        print(f"❌ Error: '{folder_path}' folder nahi mila!")
        return

    count = 0  # kitni files move hui

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Sirf files ko move karo, folders ko nahi
        if os.path.isfile(file_path):
            category = get_category(file)
            create_folder(category)

            destination = os.path.join(folder_path, category, file)
            shutil.move(file_path, destination)

            print(f"  ✅ {file}  →  {category}/")
            count += 1

    print(f"\n🎉 Done! {count} files organize ho gayi.")


# ▶️ Program chalaao
print("🚀 File Organizer Shuru Ho Raha Hai...\n")
move_files()