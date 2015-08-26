# Find all users whose friends have already been crawled
import os
folders = os.listdir('./extract')
f = []
for folder in folders:
    files = os.listdir('./extract/' + folder)
    f.extend(files)
f = map(int, f)
print f
