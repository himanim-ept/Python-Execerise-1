#Sort this dictionary ascending and descending.


import operator
d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = dict (sorted(d.items(), key=operator.itemgetter(1))) #sort in ascending
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))#sort in descending
print('Dictionary in descending order by value : ',sorted_d)


