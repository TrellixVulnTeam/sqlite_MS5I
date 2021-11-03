<<<<<<< HEAD
import random

=======
import sys
import os

import xlwings
>>>>>>> 740b4dcb2937eea9cb997703fca6fed2dbd559fa

list = ["a","b","c"]
out_list = []

<<<<<<< HEAD
total = 10000

for i in range(total):
    x = random.choice(list)
    out_list.append(x)
a = out_list.count("a")
print("a：",out_list.count("a"))
print("b：",out_list.count("b"))
print("c：",out_list.count("c"))
print("aの確率は",a/total)

=======
#file_name = r"P:\SYSTEM\購買システム\金型検収関係\金型修理履歴(仕入先手配).xls"

#App = xw.App()
#wb = App.books.open(file_name)
>>>>>>> 740b4dcb2937eea9cb997703fca6fed2dbd559fa
