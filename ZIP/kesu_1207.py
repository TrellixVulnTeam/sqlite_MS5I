import subprocess
import os
import re
import pyminizip
import shutil
import zipfile
#subprocess.run(r"C:\Users\onoga\desktop\MyDocker\Git\origin\test\opencv_createsamples.exe -info C:\Users\onoga\desktop\MyDocker\Git\origin\test\pos\poslist.txt -vec C:\Users\onoga\desktop\MyDocker\Git\origin\test\vec\positive.vec -num 1000 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 ")
#subprocess.run(r"C:\Users\onoga\desktop\MyDocker\Git\origin\test\opencv_traincascade.exe -data C:\Users\onoga\desktop\MyDocker\Git\origin\test\cascade -vec C:\Users\onoga\desktop\MyDocker\Git\origin\test\vec\positive.vec -bg C:\Users\onoga\desktop\MyDocker\Git\origin\test\neg\neglist.txt -numPos 10 -numNeg 20")

#ファイルを一括リネーム
def rename(path,cas_name):
    
    count = 1
    file = os.listdir(path)
    
    for zname in file:
        under_name = os.path.splitext(zname)[1] #拡張子取得
        new_name = os.path.join(path,zname) #取得したファイル名を絶対パスに変更
 
        os.rename(new_name,os.path.join(path,f"{cas_name}{count}{under_name}"))#リネーム
        count +=1

file_path = r"C:\Users\onoga\Desktop\ココナラ画像\囚人"
out = r'C:\Users\onoga\Desktop'
def press(dir_path):
    #fff = shutil.make_archive(f"{dir_path}","zip",root_dir=f"{dir_path}")
 
    pyminizip.compress(f"{fff}".encode("shift_jis"),"",f"{os.path.join(out,os.path.split(dir_path)[1])}.zip","dada",0)
    

#with zipfile.ZipFile("test.zip", "w",compression=zipfile.ZIP_DEFLATED,
#                                  compresslevel=9) as zf:
#    zf.write(filename=file_path)
    
press(file_path)