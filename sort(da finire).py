def sorting():
    newlist=[]
    file='romeo.txt'
    handle=open(file)
    for line in handle:
        words=line.split()
        for word in words:
            if word not in newlist:
                newlist.append(word)
        x=newlist.sort()
    return x
print(sorting())
