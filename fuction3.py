def funfcopy(source, destination):
    with open(source, 'r') as fi:
        with open(destination, 'w') as fo:
            for line in fi:
                fo.write(line)

def main():
    funfcopy('area2.txt', 'area1.txt')

if __name__ == '__main__':
    main()
