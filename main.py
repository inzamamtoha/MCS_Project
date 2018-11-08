import random as rand
from kmclustering import clustering
from point import Point
import csv

geo_locs = []
#loc_ = Point(0.0, 0.0)  #tuples for location
#geo_locs.append(loc_)

f = open('/home/inzamam/Downloads/indonesia.csv', 'r')
reader = csv.reader(f, delimiter=",")
i=1;
for line in reader:
    if i==1:
        i = 0

    else:
        loc_ = Point(float(line[0]), float(line[1]),str(line[3]))  #tuples for location
        geo_locs.append(loc_)

#print len(geo_locs)
#for p in geo_locs:
#    print "%f %f" % (p.latit, p.longit)
#let's run k_means clustering. the second parameter is the no of clusters

cluster = clustering(geo_locs,1)
flag = cluster.k_means(True)
if flag == -1:
    print "Error in arguments!"
