import os
import shutil
import sys


def copy_files(src: str, dst: str) -> None:
    """
    Recursively copy files from the source directory to the destination directory,
    organizing them into subdirectories based on their file extensions.

    Args:
        src (str): The path to the source directory.
        dst (str): The path to the destination directory.
    """
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        source_path = os.path.join(src, item)
        if os.path.isdir(source_path):
            copy_files(source_path, dst)  # Recurse into subdirectory
        elif os.path.isfile(source_path):
            # Get file extension without the dot
            ext = os.path.splitext(item)[1][1:]
            ext_dir = os.path.join(dst, ext)
            if not os.path.exists(ext_dir):
                # Create subdirectory for the file extension
                os.makedirs(ext_dir)
            try:
                shutil.copy2(source_path, ext_dir)
                print(f'Copied: {source_path} -> {ext_dir}')
            except Exception as e:
                print(f'Error copying {source_path}: {e}')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    src_directory = sys.argv[1]
    dst_directory = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    copy_files(src_directory, dst_directory)
