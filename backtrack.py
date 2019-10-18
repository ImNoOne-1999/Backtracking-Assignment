def Swap(string, start, curr):

    for i in range(start, curr):
        if string[i] == string[curr]:
            return False
    return True

def Permutations(string, index, length):

    if index == length:
        print("String : ",end=' ')
        print(''.join(string))
        return

    for i in range(index, length):
        x = Swap(string, index, i)
        if x == 1:
            string[index], string[i] = string[i], string[index]
            Permutations(string, index + 1, length)
            string[index], string[i] = string[i], string[index]


if __name__ == "__main__":

    str = list(input("Enter the string for permutations\n"))
    print("\n")
    length = len(str)
    Permutations(str, 0, length)
