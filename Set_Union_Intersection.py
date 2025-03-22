set1 = {2,2,2,4,5,6,7,8,10}
set2 = {1,2,3,4,5,6,7,8,9}
set3 = {9,8,7,5,3,2,0,4,1}

#union -set
print(set1|set2|set3)
print(set1.union(set2).union(set3))
#Intersection -set
print (set1&set2&set3)
print(set1.intersection(set2).intersection(set3))
#difference -set
print(set1-set2-set3)
print(set1.difference(set2).difference(set3))