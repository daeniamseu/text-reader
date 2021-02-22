def main():
    file = open("dummy.txt", "r", encoding="utf8")
    line = file.readlines()
    print(line[2])

    
main()
