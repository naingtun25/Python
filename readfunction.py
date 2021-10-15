def funreadletter(file_name):
    with open(file_name, 'r',encoding = 'utf-8') as fi:
        txt = fi.read()
        return txt

def main():
    print(funreadletter('Myanmar.txt'))

if __name__ == '__main__':
    main()