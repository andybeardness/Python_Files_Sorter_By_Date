# IMPORTS

import os
import sys
import time
import shutil
import datetime

# GLOBAL VARS

SYS_VARS = sys.argv

_, MAIN_DIR_NAME, NEW_DIR_NAME = SYS_VARS

# MAKE DIR WITH SORTED FILES

try:
    os.mkdir(NEW_DIR_NAME)
    print(f'[V] FOLDER \'{NEW_DIR_NAME}\' CREATED')

except FileExistsError:
    print(f'[X] ERROR! FOLDER \'{NEW_DIR_NAME}\' ALREADY EXIST!')
    exit()
    
# GET LIST OF FILES AND IT'S LENGTH IN MAIN_DIR

try:
    files     = os.listdir(MAIN_DIR_NAME)
    len_files = len(files)
    print(f'[V] FILE LIST \'{MAIN_DIR_NAME}\' CREATED')
    
except FileNotFoundError:
    print(f'[X] FOLDER \'{NEW_DIR_NAME}\' IS NOT EXIST!')
    exit()
    
# FUNC TO MAKE 2 [int] --> '02' [str] 

def int_to_02str(item):
    new_string = '{:02}'.format(item)
    return new_string
    
# MAIN FUNC

def main_loop(folder_with_files, 
              new_empty_folder, 
              list_of_files, 
              len_of_files):
    
    # MAIN LOOP TO MAKE A COPY OF EACH FILES IN NEEDED DIR

    for file in list_of_files:
        # PREPEARING. GET VARS OF CREATION TIME

        file_item  = folder_with_files + file    # EX: Camera/file001.jpg

        os_time    = os.path.getmtime(file_item) # EX: 1563646143.0
        str_time   = time.ctime(os_time)         # EX: 'Sat Jul 20 21:09:03 2019'
        date_time  = time.strptime(str_time)     # Object time.struct_time 

        file_year  = date_time.tm_year           # EX: 2019
        file_month = date_time.tm_mon            # EX: 7
        file_day   = date_time.tm_mday           # EX: 20

        str_year   = str(file_year)  + '/'       # EX: '2019/'
        str_month  = str(file_month) + '/'       # EX: '7/'
        str_day    = str(file_day)   + '/'       # EX: '20/'

        name_year  = str(file_year)  + '-'       # EX: '2019-'
        name_month = str(file_month) + '-'       # EX: '7-'


        # TRY TO MAKE YEAR DIR

        try:
            # EX: 'SORTED/2019/'
            dir_name = new_empty_folder + str_year  
            os.mkdir(dir_name)

        except FileExistsError:
            pass


        # TRY TO MAKE MONTH DIR

        try:
            # EX: 'SORTED/2019/2019-7'
            dir_name = new_empty_folder + str_year + name_year + str_month
            os.mkdir(dir_name)

        except FileExistsError:
            pass

        
        # TRY TO MAKE DAY DIR

        try:
            # EX: 'SORTED/2019/2019-7/2019-7-20'
            dir_name = new_empty_folder + str_year + name_year + str_month + name_year + name_month + str_day
            os.mkdir(dir_name)

        except FileExistsError:
            pass

        
        # GET FINALLY PATH OF COPIED FILE

        new_path = dir_name + file

        
        # COPY THIS FILE

        shutil.copyfile(file_item, new_path)

    print(f'[V] FILES COPIED: {len_of_files}')
    
# START TIME

start_time = time.time()

# START MAIN_LOOP

main_loop(folder_with_files = MAIN_DIR_NAME, 
          new_empty_folder  = NEW_DIR_NAME, 
          list_of_files     = files, 
          len_of_files      = len_files)

# END TIME

end_time = time.time()

# CALCULATING SECONDS

seconds_time = end_time - start_time

# DELTA TIME

try:
    delta_time = datetime.timedelta(seconds=seconds_time)
    print(f'[V] TIME SPENT: {delta_time}')

except:
    print(f'[?] TIME DID NOT CALCULATED :(')
    
print('[V] SCRIPT DONE!')