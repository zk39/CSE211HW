try:
    i = open("Step1Data.txt", "r")
    tempdic = {}
    booklist = []
    line = i.readlines()
    
    for x in range(1,len(line),6):
        for y in range(5):
            kv = line[x].split(': ')
            tempdic[kv[0]] = kv[1]
            x+=1
        booklist.append(tempdic)
        print(booklist)
    print(booklist)                         
except:
    print("error")

# print(booklist)
# def displayBook(name):
#     for book in booklist:
#         print(book['Key'])
#         if book["Key"]==name: 
#             print('a')
# 
# displayBook("Rowling1997") 