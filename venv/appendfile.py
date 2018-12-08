global file
file='file.txt'

try:
    with open(file,'a',encoding="utf-8") as f:
        f.write("I like python")
except Exception as e:
    print(e)



