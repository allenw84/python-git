import os
files = []

for f in os.listdir('.'):
        if os.path.isfile(f):
                files.append(f)
for f in files:
        print f 