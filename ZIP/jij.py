import os

path  = "file:///C:/Users/onoga/Desktop/icon32.ico"
bas = "C:/Users/onoga/Desktop/icon32.ico"



file_path =path
#ドラッグ＆ドロップ時のfile:///を消去
input_path = file_path.lstrip("file:///")


file_full_name = os.path.split(input_path)[1]
file_name =  os.path.splitext(file_full_name)[0]

#os.chdir(__path__)
print(file_full_name)