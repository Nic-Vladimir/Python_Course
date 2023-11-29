filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f'Files/{filename}', 'r')
    content = file.read()
    print(content.title())
