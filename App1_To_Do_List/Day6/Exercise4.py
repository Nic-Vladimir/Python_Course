filenames = ["doc.txt", "reports.txt", "presentation.txt"]

for filename in filenames:
    file = open(f'Files/Ex4/{filename}', 'w')
    file.write('Hello')
    file.close()
    