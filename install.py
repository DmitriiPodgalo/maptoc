import os

PATH = os.environ['PATH'].split(':')[0]

path = os.path.join(PATH, 'maptoc')
with open('maptoc') as inf, open(path, 'w') as ouf:
    ouf.write(inf.read())
    os.chmod(path, 0o777)

print('Files added to', PATH)
