import json
import pickle

# str(function) gibt nh memory Adresse aus
def test(n):
    return n * 2 + 3

stuffToWrite = ("string",1,["List"],{"Dictionary":"Value"},(1,2),True,False,1.0)
stuffToWritePickle = stuffToWrite + ({1,2},1+2j,test)
with open("Test.txt", "w") as f:
    for stuff in stuffToWritePickle:
        # need to convert to str
        f.write(str(stuff))
        f.write("\n")

# cant write set, complex and function to json
json.dump(stuffToWrite, open("Test.json", "w"))
pickle.dump(stuffToWritePickle, open("Test.pickle", "wb"))