import random


list = ["a","b","c"]
out_list = []

total = 10000

for i in range(total):
    x = random.choice(list)
    out_list.append(x)
a = out_list.count("a")
print("a：",out_list.count("a"))
print("b：",out_list.count("b"))
print("c：",out_list.count("c"))
print("aの確率は",a/total)

