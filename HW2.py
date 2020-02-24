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
            if tempdic["Key"]==name:
                displayTempdic(tempdic)
    except:
        print("奥利给")

def displayTempdic(dic):
    skey = removen(dic, 'Key')
    
    AuthorName = dic["Author"].split(" ")
    AuthorName[1] = AuthorName[1][0:len(AuthorName[1])-1]
    sname = AuthorName[1]+", "+AuthorName[0] 
    
    title = removen(dic,'Title')
    publisher = removen(dic, "Publisher")
    date = removen(dic, "Date")
    
    book = [sname, title, publisher,date]
    s = ', '
    print(skey+"    "+s.join(book)+".")
    
def removen(dic,head):
    temp = dic[head].split("\n")
    ss = temp[0] 
    return ss

val = input("Enter your Key: ")
displayBook(val) 