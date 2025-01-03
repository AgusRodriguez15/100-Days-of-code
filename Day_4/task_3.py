#Figure out how to pick a random name from the list of friends.
#
# Hint 1 
#There are two ways of doing this and they are equally valid.
# Hint 2 
#Think about how you can generate random number to use an index to pick out items from the List.
# Hint 3 
#Alternatively think about using the documentation to figure out how to get a random item from a List in Python.

#import random
# the first way that i think
#friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#num = random.randint(0, 4)
#print(friends[num])

import random
# the second way that i think
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))
