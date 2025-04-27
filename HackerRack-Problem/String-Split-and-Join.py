def split_and_join(line):
    splitedString=line.split(' ')
    return '-'.join(splitedString)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)