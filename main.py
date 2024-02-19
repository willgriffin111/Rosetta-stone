
# Dictionary to store encryption mappings 
cipherDict = {}

# Function to learn from the provided data and populate the dictionary
def learn(data):
    # Read lines from the provided data
    lines = data.readlines()
    
    # Iterate over each line
    for x, line in enumerate(lines):
        # Skip the first line 
        if x == 0:
            continue
        # Remove leading and trailing whitespaces from the line
        line = line.strip()
        # Split the line into the key and value
        ind = line.split("|")
        # Add the mapping to the dictionary
        cipherDict[ind[0]] = ind[1]

# Function to decrypt the provided data
def decrypt(data):
    # Read a line of data and split it into individual components 
    line = data.readline().strip().split(" ")
    # List to store the decrypted output
    output = []
    # Variable to store a collection words to decrypt together
    collection = ""
    # Flag to indicate whether the input is integer
    isInt = False
    
    try:
        # Check if the first element of the line can be converted to an integer
        if isinstance(int(line[0][2:]), int):
            isInt = True
    except:
        isInt = False
            
    # If the input starts with an integer
    if isInt:
        # Iterate over each number
        for indNums in line:
            # String to store the decrypted results
            intDecrypted = ""
            
            # Iterate over the integers in pairs
            for i in range(0, len(indNums), 2):
                # Extract a pair of integers from the encoded number
                numPairs = indNums[i:i+2]
                # Decrypt the pair and append it to the decrypted string
                intDecrypted += cipherDict[numPairs]
            # Append the decrypted integer to the output list
            output.append(intDecrypted)
    else:
        # If the input contains words
        for word in line:
            # Build a collection of consecutive words until a match is found in the dictionary
            if collection:
                newCollection = collection + " " + word
            else:
                newCollection = word
            
            # Check if the new collection exists in the dictionary
            if newCollection in cipherDict:
                collection = newCollection
            else:
                # If the collection does not exist in the dictionary
                if collection:
                    # Append the decrypted counterpart of the collection to the output list
                    output.append(cipherDict[collection])
                    # Reset the collection
                    collection = ""
                # Check if the current word exists in the dictionary
                if word in cipherDict:
                    # Append the decrypted counterpart of the word to the output list
                    output.append(cipherDict[word])
                else:
                    # If the word is not found in the dictionary, treat it as a new collection
                    collection = word
            
        # Check if there's any remaining collection to decrypt
        if collection in cipherDict:
            # Append the decrypted counterpart of the collection to the output list
            output.append(cipherDict[collection])
        else:
            # If the collection is not found in the dictionary, append it as is
            output.append(collection)

    # Return output as string 
    return " ".join(output)


# Main program starts here
print("LEARN")
learn(open("Rosetta-stone/data/test1.txt", "r"))
learn(open("Rosetta-stone/data/test2.txt", "r"))
learn(open("Rosetta-stone/data/test3.txt", "r"))
# Print the dictionary after learning
print(cipherDict)

# Decrypt and print data from test files
print("DECRYPT")
print(decrypt(open("Rosetta-stone/data/test1.txt", "r")))
print(decrypt(open("Rosetta-stone/data/test2.txt", "r")))
print(decrypt(open("Rosetta-stone/data/test3.txt", "r")))
