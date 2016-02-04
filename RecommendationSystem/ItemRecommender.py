'''
Created on Nov 28, 2015

@author: tedmarchildon
'''

import RecommenderEngine, json
import BookReader

if __name__ == "__main__":
    (jitems,jratings) = BookReader.getData("bookratings.txt")
    print "items = ",jitems
    print "ratings = ", jratings
    
    items = json.loads(jitems)
    ratings = json.loads(jratings)
    
    avg = RecommenderEngine.averages(items,ratings)
    #print avg
     
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
        print key,slist
        print "\t",RecommenderEngine.scores(slist,items,ratings,1)
        print "\t",RecommenderEngine.scores(slist,items,ratings,len(slist))
        print '\t', RecommenderEngine.recommend(key, items, ratings, 3)
