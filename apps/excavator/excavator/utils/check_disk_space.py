import shutil
import os
import platform

def get_drive_path():
    """
    Determines the appropriate drive path based on the operating system.
    - On Windows, returns current drive letter (e.g., C:\\).
    - On macOS/Linux, returns root directory (/).
    """
    system = platform.system()
    if system == "Windows":
        return os.path.splitdrive(os.getcwd())[0] + "\\"
    else:
        return "/"

def get_disk_usage(path):
    """
    Returns disk usage statistics about the given path as a dictionary.
    Values are in gigabytes (GB).
    """
    total, used, free = shutil.disk_usage(path)
    gb = 1024 ** 3
    return {
        'Total': round(total / gb, 2),
        'Used': round(used / gb, 2),
        'Free': round(free / gb, 2)
    }