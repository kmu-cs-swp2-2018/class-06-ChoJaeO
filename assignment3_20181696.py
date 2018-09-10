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
        length = len(parse)
        if parse[0] == 'add':
            if length > 4:
                print("Error : You should input parse maximum three")
                continue
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
		print("Add Complete")
            except:
                continue
        elif parse[0] == 'find':
            if length > 2:
                print("Error : You should input parse maximum one")
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
            inc_num = 0
            if length > 3:
                print("Error : You should input parse maximum two")
                continue
            try:
                for p in scdb:
                    if p['Name'] == parse[1]: 
                        p['Score'] = str(int(p['Score'])+int(parse[2]))
                        inc_num += 1
                print("Increase" + inc_num + "student(s) score")
            except:
                continue
        elif parse[0] == 'del':
            if length > 2:
                print("Error : You should input parse maximum one")
                continue
            try:
                del_num = 0
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                        del_num += 1
                print("Delete" + del_num + "student(s)")
            except:
                continue
        elif parse[0] == 'show':
            if lenght > 1:
                print("Error : You don't need to input more parse")
                continue
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            if length > 1:
                print("Error : You don't need to input more parse")
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
