f=open("file.txt")
count=0
l=f.readlines()
for eachline in l:
    words=eachline.split()
    count=count+len(words)

print(count)
