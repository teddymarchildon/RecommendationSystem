'''
Created on Nov 27, 2015

@author: tedmarchildon
'''
import operator

def match(list, dict):
    '''
    This function takes the items in a list and makes them the keys of a dictionary, 
    and takes the values in the dictionary and takes only those values at the index of
    the item in the list and appends them to the value at that item. So it takes the
    ratings for each item in the list and puts them in a dictionary.
    '''
    
    d = {}
    i = 0
    for item in list:
        for key in dict:
            if item not in d:
                if dict[key][i] != 0:
                    d[item] = [dict[key][i]]
            elif dict[key][i] != 0:
                d[item].append(dict[key][i])
        i += 1
    return d


def averages(items, ratings):
    '''
    This function takes the dictionary returned by the match function and makes the average
    of the ratings the value at that key.
    '''
    d = match(items, ratings)
    for key in d:
        length = len(d[key]) + 1
        d[key] = float(sum(d[key]))/(length)
    ret = []
    for (item, rating) in d.items():
        ret.append((item, rating))
    ret1 = sorted(ret)
    return sorted(ret1, key = operator.itemgetter(1), reverse = True)
        
def dotproduct(list1, list2):
    '''
    This function takes the dot product of the values in two lists and returns
    an integer
    '''
    ret = []
    j = 0
    for i in list1:
        a = list2[j]
        ret.append(i*a)
        j += 1
    return sum(ret)

def similarities(name, ratings):
    '''
    This function finds the similar items based on the dotproduct of their rankings, 
    and returns a sorted list of tuples with the items and the dotproduct sorted
    numerically descending and then alphabetically
    '''
    d = {}
    for key in ratings:
        if key != name:
            dp = dotproduct(ratings[name], ratings[key])
            d[key] = dp
    ret = []
    for (k, v) in d.items():
        ret.append((k,v))
    ret1 = sorted(ret)
    return sorted(ret1, key = operator.itemgetter(1), reverse = True)
    
def matchWithZero(list, dict):
    '''
    This function is the same as the match function above, but it includes zeros
    '''
    d = {}
    for i in range(len(list)):
        for key in dict:
            if list[i] not in d:
                d[list[i]] = dict[key][i]
            else:
                d[list[i]] += dict[key][i]
    return d

def weight(slist, ratings):
    '''
    This function weights the ratings based on the dotproduct of those ratings and the
    ratings of the user given in similarities
    '''
    d = {}
    for (k, v) in slist:
        d[k] = [v * i for i in ratings[k]]
    return d

def scores(slist,items,ratings,n):
    '''
    This function returns the scores of items rated based on the person given in 
    the similarities function and returns a sorted list of tuples
    '''
    d = weight(slist, ratings)
    a = matchWithZero(items, d)
    ret = [(k, v) for (k, v) in a.iteritems()]
    ret1 = sorted(ret)
    return sorted(ret1, key = operator.itemgetter(1), reverse = True)[:n]
        
def recommend(name, items, ratings, count):
    '''
    This item makes recommendations based on the score, and returns a sorted list of
    tuples with the item, the score with the person rating the item, and the average
    score of that item for all people
    '''
    a = similarities(name, ratings)
    b = averages(items, ratings)
    c = scores(a, items, ratings, count)
    ret = []
    i = 0
    for (x, y) in c:
        z = b[i][1]
        ret.append((x, y, z))
        i += 1
    ret1 = sorted(ret)
    return sorted(ret1, key = operator.itemgetter(1), reverse = True)
        
    