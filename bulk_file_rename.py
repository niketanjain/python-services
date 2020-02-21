from os import rename, listdir

path = "Your Path of Files"

for file_name in listdir(path):
  new_file_name = "Your New File Name with File Extension"
  rename(file_name, new_file_name)
  
