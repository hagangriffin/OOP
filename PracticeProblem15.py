import pickle

#d = {"e":1}

#with open("students.dat", "wb") as file1:
    #pickle.dump(d, file1)
#file1.close()

with open("students.dat", "rb") as file2:
    myDictionary = pickle.load(file2)
file2.close()
print(myDictionary["e"])

i=1
for e in myDictionary:
    var = "stu"+str(i)
    print(myDictionary[var]["Name"])
    i+=1
