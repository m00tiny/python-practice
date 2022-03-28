if __name__ == '__main__':
    N = int(input())
    while N > 0:
        myArray = list()
        cmd = input().split()
        x,y = [cmd[int(1):int(2)]
        if cmd[0] == "insert":
            myArray.insert[x,y]
        elif cmd[0] == "print":
            print (myArray)
        elif cmd[0] == "remove":
            myArray.remove(cmd[1])
        elif cmd == "append":
            myArray.append(cmd[1])
        elif cmd == "sort":
            myArray = myArray.sort()
        elif cmd == "pop":
            myArray = myArray.pop()
        elif cmd == "reverse":
            myArray = myArray.reverse()
