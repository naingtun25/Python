def funfcopy(source, destination):
    fi = open(source, 'r')
    fo = open(destination, 'w')
    for line in fi:
        fo.write(line)
    fo.close()
    fi.close()
def main():
    funfcopy('area2.txt', 'area3.txt')

if __name__ == '__main__':
    main()