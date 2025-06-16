import os
from pathlib import Path

def generate_tree(directory=".", output_file="structure.txt", ignore_list=None):
    if ignore_list is None:
        ignore_list = [".git", "node_modules", "__pycache__", ".DS_Store"]
    
    def print_tree(path, prefix="", file_handle=None):
        path = Path(path)
        entries = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        
        for index, entry in enumerate(entries):
            if entry.name in ignore_list:
                continue
            connector = "└── " if index == len(entries) - 1 else "├── "
            print(f"{prefix}{connector}{entry.name}", file=file_handle)
            
            if entry.is_dir():
                extension = "    " if index == len(entries) - 1 else "│   "
                print_tree(entry, prefix + extension, file_handle)
    
    with open(output_file, "w", encoding="utf-8") as f:
        print(".", file=f)
        print_tree(directory, file_handle=f)

if __name__ == "__main__":
    # Customize the directory and ignore list as needed
    project_dir = "."  # Current directory; change to your project path
    ignore = ["gen_dir_tree.py", "structure.txt", ".vs", ".venv", ".git", "node_modules", "__pycache__", ".DS_Store"]
    generate_tree(project_dir, "structure.txt", ignore)