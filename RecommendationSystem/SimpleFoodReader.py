
import json

def readDatafile (filename):
    """
    given a filename that is formatted as comma separated values,
    return a list of lists of strings, where each line is represented
      as a list of separate string elements
    """
    f = open(filename)
    result = [ line.strip().split(',') for line in f.readlines() if len(line) > 1 ]
    f.close()
    return result


def convertStrings (statList):
    """
    given a list of strings representing int values,
      return a list of ints, the converted values of the strings
    """
    return [ int(s) for s in statList ]


def getData (filename):
    """
    given the name of a file of data about restaurant ratings, 
      returns two sequences: a list of strings, the restaurant names in file order,
      and a dictionary of strings as the key and a list of ints as the values, the
      raters and their ratings of the books
    """
    data = readDatafile(filename)
    itemList = [ d[0] for d in data if len(d) == 1 ]
    #print itemList
    # ratings are those lines with multiple items (i.e., commas between ratings)
    ratingsDict = {}
    for line in data:
        if len(line) > 1:
            rater = line[0]
            ratings = convertStrings(line[1:])
            ratingsDict[rater] = ratings
    return (json.dumps(itemList), json.dumps(ratingsDict))

if __name__ == "__main__":
    (items,ratings) = getData("foodratings_example.txt")
    print"items = ",items
    print"ratings = ", ratings
    
    print type(items), type(ratings)

    var = json.loads(items)
    print type(var),var
    print len(var)
    dvar = json.loads(ratings)
    print type(dvar),dvar
    print len(dvar['student1004'])
