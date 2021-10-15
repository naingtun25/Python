def funmyfont(file_name, msg):
    with open(file_name, 'a',encoding='utf-8') as fo:
        fo.write(msg)

def main():
    funmyfont('myanmar.txt', '\nမင်္ဂလာပါ')

if __name__ == '__main__':
    main()
    