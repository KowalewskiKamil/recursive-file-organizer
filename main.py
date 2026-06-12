import os
import shutil
from pathlib import Path

USER_PROFILE = os.environ.get('USERPROFILE') or os.environ.get('HOME')
DOWNLOADS_PATH = os.path.join(USER_PROFILE, 'Downloads')
BASE_FOLDER = Path(DOWNLOADS_PATH)

TYPES = {
    '.jpg': 'Pliki_jpg',
    '.jpeg': 'Pliki_jpeg',
    '.png': 'Pliki_png',
    '.pdf': 'Pliki_pdf',
    '.webp': 'Pliki_webp',
    '.bmp': 'Pliki_bmp',
    '.tif': 'Pliki_tiff',
    '.tiff': 'Pliki_tiff',
    '.gif': 'Pliki_gif',
    '.c': 'Pliki_c',
    '.cpp': 'Pliki_cpp',
    '.txt': 'Pliki_txt',
    '.m': 'Pliki_MATLAB_m',
    '.xlsx': 'Pliki_EXCEL_xlsx',
}
BLOCKED = set(TYPES.values())
BLOCKED.add('Pliki_inne')

def file_sort(current_folder):
    if not current_folder.exists() or not current_folder.is_dir():
        return 0
    moved_files = 0
    for element in current_folder.iterdir():
        if element.is_file():
            file_type = element.suffix.lower()
            if file_type in TYPES:
                folder_name = TYPES[file_type]
                target_folder = BASE_FOLDER / folder_name
                target_folder.mkdir(exist_ok=True)
                new_file_path = target_folder / element.name
            else:
                print(f"File {element.name} does not match any kind of file.")
                folder_name = 'Pliki_inne'
                target_folder = BASE_FOLDER / folder_name
                target_folder.mkdir(exist_ok=True)
                new_file_path = target_folder / element.name
            if not new_file_path.exists():
                shutil.move(str(element), str(new_file_path))
                print(f"Moved: {element.name} -> {folder_name}/")
                moved_files += 1
        elif element.is_dir():
            if element.name in BLOCKED:
                continue
            print(f"Entering subfolder: {element.relative_to(BASE_FOLDER)}")
            moved_files += file_sort(element)
    return moved_files

if __name__ == "__main__":
    print(f"File sorting started in: {BASE_FOLDER.resolve()}\n")
    total_moved = file_sort(BASE_FOLDER)
    print(f"\nProcess succeeded! Total moved files: {total_moved}")