import os
import logging
from collections import namedtuple
from argparse import ArgumentParser

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def collect_info(directory_path):
    if not os.path.isdir(directory_path):
        raise ValueError(f"Chosen path {directory_path} is not directory.")
    
    parent_directory = os.path.basename(os.path.abspath(directory_path))
    
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        
        if os.path.isdir(entry_path):
            file_info = FileInfo(name=entry, extension=None, is_directory=True, parent_directory=parent_directory)
        else:
            name, extension = os.path.splitext(entry)
            file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)
        
        logging.info(f'{file_info.name} | {file_info.extension if file_info.extension else "N/A"} | {"Directory" if file_info.is_directory else "File"} | {file_info.parent_directory}')

def main():
    parser = ArgumentParser(description="Collecting info contrnts of directory & writing to log.")
    parser.add_argument('directory', type=str, help="Path to directory")
    args = parser.parse_args()
    directory_path = args.directory
    
    try:
        collect_info(directory_path)
        print(f'Info contents of directory "{directory_path}" succeed writing "directory_contents.log".')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()

# Для запуска: python task5.py C:\Users\ghost\Desktop\Exam1 либо указать другой