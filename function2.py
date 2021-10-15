def funfcopy(file_name):
    with open(file_name, 'r') as f:
        txt = f.read()
        print(txt)  
def main():
    funfcopy('area.py')

if __name__ == '__main__':
    main()