#!/usr/bin/env python3
import os 
from datetime import datetime

files_to_check = []
files = []

def isWorkDay() -> bool:
    return True

def get_file_date(file_path) -> datetime:
    timestamp = os.path.getmtime(file_path)
    modification_date = datetime.fromtimestamp(timestamp)
    return modification_date

def count_files(dir: str) -> int: 
    count = 0 
    list_dir = list(os.scandir(dir)) 
    for file in list_dir: 
        if file.is_file(): 
            count += 1
            file_name = file.name
            file_path = f'{dir}\\{file_name}'
            file_date = get_file_date(file_path)
            file_object = {"name": file_name, "date": file_date}
            files.append(file_object)
    return count

args = { 
    'path': 'C:\\Users\\cezar\\Documents\\nextios\\lab_folder', 
}
directory = args['path'] 
try: 
    file_counter = count_files(directory)
    index = 0
    for file in files:
        name = file['name']
        date = file['date']
        print(f'{index}\n')
        print(f'File: {name}')
        print(f'Date: {date}')
    print (f'\n\tTotal: {file_counter}\n')
except Exception as e: 
    print(f'Error: {e}')