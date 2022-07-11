import os 

dir_path = "C:/Users/onoga/Desktop/MyDocker/Git/sqlite/onogam/6_3da/pos"
os.chdir(dir_path)
file_list = os.listdir(dir_path)
lsiin = [s for s in file_list if ".txt" not in s]
print(lsiin)