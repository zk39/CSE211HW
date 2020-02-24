def displayBook(name):
    name = name+"\n"
    try:
        i = open("Step1Data.txt", "r")
        tempdic = {}
        line = i.readlines()
    
        for x in range(1,len(line),6):
            for y in range(5):
                kv = line[x].split(': ')
                tempdic[kv[0]] = kv[1]
                x+=1
#             booklist.append(tempdic)
            if tempdic["Key"]==name:
                displayTempdic(tempdic)
    except:
        print("奥利给")

def displayTempdic(dic):
    tempKey = dic["Key"].split("\n")
    skey = tempKey[0]
    
    AuthorName = dic["Author"].split(" ")
    AuthorName[1] = AuthorName[1][0:len(AuthorName[1])-1]
    sname = AuthorName[1]+", "+AuthorName[0] 
    
    temptitle = dic["Title"].split("\n")
    title = temptitle[0]
    
    tempPublisher = dic["Publisher"].split("\n")
    publisher = tempPublisher[0]
    
    tempDate = dic["Date"].split("\n")
    date = tempDate[0]
    
    book = [sname, title, publisher,date]
    s = ', '
    print(skey+"    "+s.join(book)+".")
    

val = input("Enter your Key: ")
displayBook(val) 