import os
import shutil
file_name = 'states.txt'
temp_name = "temp.txt"

# shutil.copy(file_name, file_name + ".orig")

with open(file_name) as file_in:
    with open(temp_name, "w") as file_out:
        for line in file_in:
            new_line = line.upper()
            file_out.write(new_line)

os.rename(file_name, file_name + '.BAK') # states.txt --> states.txt.BAK
os.rename(temp_name, file_name)  # temp.txt --> states.txt
