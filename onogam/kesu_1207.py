import subprocess
import os

#subprocess.run(r"C:\Users\onoga\desktop\MyDocker\Git\origin\test\opencv_createsamples.exe -info C:\Users\onoga\desktop\MyDocker\Git\origin\test\pos\poslist.txt -vec C:\Users\onoga\desktop\MyDocker\Git\origin\test\vec\positive.vec -num 1000 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 ")
#subprocess.run(r"C:\Users\onoga\desktop\MyDocker\Git\origin\test\opencv_traincascade.exe -data C:\Users\onoga\desktop\MyDocker\Git\origin\test\cascade -vec C:\Users\onoga\desktop\MyDocker\Git\origin\test\vec\positive.vec -bg C:\Users\onoga\desktop\MyDocker\Git\origin\test\neg\neglist.txt -numPos 10 -numNeg 20")

file = os.listdir(r"C:\Users\60837\Desktop\Resized_1")
print(file)