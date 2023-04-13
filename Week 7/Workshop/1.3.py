input_file_opened = False
while not input_file_opened:
    try:
        file_name = input("Enter file name")
        input_file = open(file_name, 'r')
        input_file_opened = True
    except: print('Input file not found')