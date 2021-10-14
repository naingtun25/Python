f = open('Note from Drive.py', 'r')
txt = f.read(10)
while(len(txt) > 0):
    print(txt,end="*")
    txt = f.read(10)
f.close()