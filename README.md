# Recursive File Organizer

A simple and efficient Python script that recursively scans your Downloads folder (and all its subdirectories) and organizes files into specific folders based on their extensions.

## Features
- **Recursive Scan:** Goes deep into all subfolders.
- **Safety First:** Avoids infinite loops by blocking destination folders.
- **Universal:** Automatically detects the current user's Downloads directory.
- **Catch-all:** Moves unrecognized file types to a default `Pliki_inne` folder.

## How to use
Simply run the script using Python 3:
```bash
python file_organizer.py
