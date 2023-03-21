import os
import sys
import shutil
import time

# This checks if the number of arguments is correct
# If the number of arguments is incorrect (len(sys.argv) != 3) print error message and exit
if len(sys.argv) != 3:
    print("backup.py target_directory_name destination_directory_name")
    sys.exit()

# This checks if argument 1 and argument 2 are valid directory paths
if not os.path.isdir(sys.argv[1]) or not os.path.isdir(sys.argv[2]):
    print("Invalid directory path provided")
    sys.exit()

#Getting target and destination directories
target_directory = sys.argv[1]
destination_directory = sys.argv[2]


print("Target Directory: " + target_directory)
print("Destination Directory: " + destination_directory)

#Using current time
current_ts = int(time.time())

#Naming backup file to current time in seconds 
backup_file_name = "backup-[{0}].tar.gz".format(current_ts)


# 1: Go into the target directory
orig_abs_path = os.getcwd()


os.chdir(destination_directory)
dest_dir_abs_path = os.getcwd()


os.chdir(orig_abs_path)
os.chdir(target_directory)


yesterday_ts = current_ts - 24 * 60 * 60

to_backup = []

for file in os.listdir():
    if os.path.isfile(file) and os.path.getmtime(file) > yesterday_ts:
        to_backup.append(file)


tar_cmd = "tar -czvf {0} {1}".format(backup_file_name, " ".join(to_backup))
os.system(tar_cmd)


shutil.move(backup_file_name, dest_dir_abs_path)