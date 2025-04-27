def swap_case(s):
    swapedString =[]
    for i in s:
        if (i.upper()==i):
            swapedString.append(i.lower())
        else:
            swapedString.append(i.upper())
    return ''.join(swapedString)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)