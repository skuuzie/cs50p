def main():
    filename = input("File name: ")

    if '.' not in filename:
        print('application/octet-stream')
        return

    extension = filename.split('.')[-1].lower().rstrip()

    if extension == 'gif':
        print('image/gif')
    elif extension == 'jpeg' or extension == 'jpg':
        print('image/jpeg')
    elif extension == 'png':
        print('image/png')
    elif extension == 'pdf':
        print('application/pdf')
    elif extension == 'txt':
        print('text/plain')
    elif extension == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')

main()
