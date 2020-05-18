#!/usr/bin/python3
def main():
    def include():
        for a in arrList:
            print("insert into {}({}) values ({});".format(tableName, columnName, a))

    def not_include():
        for a in arrList:
            print("insert into {} values ({});".format(tableName, a))

    i = 0
    arrList = []
    tableName = str(input("\nPlease Enter Table Name : "))

    column = int(input("\nColumn Name include? \n (1)include : (2)not include : "))

    if column == 1:
        columnName = str(input("Please enter column name : "))

    n = int(input("\nHow many times? : "))
    while i in range(0, n):
        print("Say :", i, ": ")
        i += 1
        arr = str(input())
        arrList.append(arr)
        # print("List is :",arrList)

    if column == 1:
        include()

    elif column == 2:
        not_include()


if __name__ == '__main__':
    main()
