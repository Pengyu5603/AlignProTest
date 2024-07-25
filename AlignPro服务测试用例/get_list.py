import os

path = 'imagetype=4'
files = os.listdir(path)
files = [file.split('_')[0] for file in files]
files = list(set(files))

print(files)