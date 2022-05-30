import os
import glob
import re

#grabでフォルダの中のファイルを検出
def main(name):
    #*[(（]と記載する事で()の大文字と小文字両方引っかけれる
    
    uu_no = []
    uuu_yes = []
    x = glob.glob("{}/*-*[(（)）]*[.xlsx.xls.pdf]?".format(name))
    print(x)
    for ii in x:
        #if re.search("[~$]", ii): #re.search("[~$]")で~$を含むファイルを抽出している
        #    uu_no.append(ii)
        #else:
            uuu_yes.append(ii)
    return uuu_yes


#fds =os.listdir(r"C:\Users\60837\Desktop\てｓｓ")

#for i in fds:
#    if i.endswith(".xls") == True:
#        print(f"{i} = YES")
        
#    else:
#        print(f"{i} = NO")
os.chdir(r"C:\Users\60837\Desktop\てｓｓ")
filename = "260-740-D09W-50M38A-1(メンテ)高橋.xls"

print(os.path.splitext(filename))
