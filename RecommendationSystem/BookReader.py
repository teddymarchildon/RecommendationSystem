'''
Created on Nov 27, 2015

@author: tedmarchildon
'''
import json

def readDatafile (filename):
    """
    given a filename that is formatted as comma separated values,
    return a list of lists of strings, where each line is represented
    as a list of separate string elements
    """
    f = open(filename)
    result = [ line.strip().split(',') for line in f.readlines() ]
    f.close()
    return result
#print readDatafile("bookratings.txt")

def getData(filename):
    '''
    Returns json strings of the list of items being rated and a json dictionary of
    the raters as keys and the ratings as values
    '''
    
    data = readDatafile(filename)
    itemList = []
    for item in data:
        itemList.extend([ item[i] for i in range(1, len(item), 2) ])
        break
    ratingsDict = {}
    for line in data:
        if len(line) > 1:
            rater = line[0]
            ratings = [int(line[i]) for i in range(2, len(line), 2)]
            ratingsDict[rater] = ratings
    #print ratings
    return (json.dumps(itemList), json.dumps(ratingsDict))
    
#getData("bookratings.txt")


if __name__ == "__main__":
    (items,ratings) = getData("bookratings.txt")
    print"items = ",items
    print"ratings = ", ratings
    
    print type(items), type(ratings)
    
    var = json.loads(items)
    print type(var),var
    dvar = json.loads(ratings)
    print type(dvar),dvar
