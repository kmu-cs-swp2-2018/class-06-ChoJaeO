import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        l = len(parse)
        if parse[0] == 'add':
            if l > 4:
                print("Error")
                continue
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except:
                continue
        elif parse[0] == 'find':
            if l > 2:
                print("Error")
                continue
            find_person = []
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        find_person += [p]
                showScoreDB(find_person, 'Name')
            except:
                continue
        elif parse[0] == 'inc':
            if l > 3:
                print("Error")
                continue
            try:
                for p in scdb:
                    if p['Name'] == parse[1]: 
                        p['Score'] = str(int(p['Score'])+int(parse[2]))
            except:
                continue
        elif parse[0] == 'del':
            if l > 2:
                print("Error")
                continue
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except:
                continue
        elif parse[0] == 'show':
            if l > 1:
                print("Error")
                continue
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            if l > 1:
                print("Error")
                continue
            break
        else:
            print("Invalid command: " + parse[0])
        
def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
