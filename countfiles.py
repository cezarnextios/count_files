#!/usr/bin/env python3
import os 
from datetime import datetime, date, time

files_to_check_cartoes = [
    "cart_baseiof.csv",
    "cart_plan_camp.csv",
    "cart_rot_combinado.csv",
    "cart_saldodevmin.csv",
    "CartoesPAGTOMIN.csv",
    "CartoesREGRACAMPANHA.csv",
    "Cartoestxcamp.csv"
]

files_to_check_matera = [
    "mat_Cadoc.csv",
    "mat_CC.csv",
    "mat_CC_acumulativo.csv",
    "mat_CC_ANUAL.csv",
    "mat_CC_atual.csv",
    "mat_Vers_Matera.csv",
]

files = []

def lengthEqual(array,number):
    return  number == len(array) 

def contains(text,array):
    return text in array
        
def is_today(date_time):
    today = date.today()
    return date_time == today

def is_on_time(file_time):
    max_time = time(12,30,0)
    return file_time < max_time

def get_file_date(file_path) -> datetime:
    timestamp = os.path.getmtime(file_path)
    to_datetime = datetime.fromtimestamp(timestamp)
    separate_datetime = {
        "date": to_datetime.date(),
        "time": to_datetime.time()
    }
    return separate_datetime

def count_files(dir: str) -> int: 
    count = 0 
    list_dir = list(os.scandir(dir)) 
    for file in list_dir: 
        if file.is_file(): 
            count += 1
            file_name = file.name
            file_path = f'{dir}\\{file_name}'
            file_date = get_file_date(file_path)
            file_object = {"name": file_name, "date": file_date['date'], "time": file_date['time']}
            files.append(file_object)
    return count

args = { 
    'path_cartoes': 'C:\\Users\\cezar\\Documents\\nextios\\lab_folder\\cartoes',
    'path_matera': 'C:\\Users\\cezar\\Documents\\nextios\\lab_folder\\matera'
}
directory_cartoes = args['path_cartoes']
directory_matera = args['path_matera'] 
try: 
    file_cartoes = count_files(directory_cartoes)
    index = 0
    count_ok = 0
    for file in files:
        file_name = file['name']
        file_date = file['date']
        file_time = file['time']
        contain = contains(file_name,files_to_check_cartoes)
        today = is_today(file_date)
        on_time = is_on_time(file_time)
        print(contain, today, on_time)
        if contain and today and on_time:
            count_ok = count_ok + 1
        index = index + 1
    size = lengthEqual(files_to_check_cartoes,count_ok)
    print('count',count_ok)
    print('size',len(files_to_check_cartoes) )
    if size:
        print (1)
    else:
       print (0) 
except Exception as e: 
    print(f'Error: {e}')