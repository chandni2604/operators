global file
file='file.txt'
try:
    with open(file,'w',encoding="utf-8" ) as f:
        f.write("\nChandni")
except Exception as e:
    print(e)

