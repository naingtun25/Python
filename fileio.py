#fileio.py

f = open('Circleofarea.py','r')
print(f.name)
print(f.mode)
print(f.closed)
f.close()
print(f.closed)