
def open_file():
    while True:
        try:
            file_name = input('Enter name of file')
            file = open(file_name, 'r')
        except FileNotFoundError:
            print('Enter real  name of file')
        else:
            return file

file = open_file()

print('\nIn file')
for line in file.readlines():
    print(line.strip('\n'))

file.close()