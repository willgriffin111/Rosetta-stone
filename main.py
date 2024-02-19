import os


cipherDict = {}

def learn(data):
    lines = data.readlines()

    for x,line in enumerate(lines):
        if x == 0:
            continue
        line = line.strip()
        ind = line.split("|")
        cipherDict[ind[0]] = ind[1]


def decrypt(data):
    output = []
    line = data.readlines()[0].strip().split(" ")


    for word in line:
        if word in cipherDict:
            output.append(cipherDict[word])
        else:
            output.append(word)
    
    return " ".join(output)



print("LEARN")
learn(open("Rosetta-stone/data/test1.txt","r"))
print(cipherDict)
print("DECRYPT")
print(decrypt(open("Rosetta-stone/data/test1.txt","r")))



# for fileName in sorted(os.listdir("Rosetta-stone/data")):
#     print(fileName)
    
    # # Check if the file is a result file
    # if fileName.startswith("GridSearchResults") and fileName.endswith(".txt"):
    #     # Open the file
    #     with open(os.path.join(resultsFileDirectory, fileName), 'r') as file: