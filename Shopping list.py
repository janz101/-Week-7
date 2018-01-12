#Demonstrate properties of Lists

#create a list

container=["orange,Banana",9.99,75-10,["celery,cumcumber"]]

#print contents of container
print("container is", container)

#Access items using an index
print("container[0]is",container[0])
print("container[4]is",container[4])
print("container[-1]is",container[-1])
print("container[-1][1]is",container[-1])
print("container[-1][1]is",container[-1][1])

#Mutating(modifying items in a list)
print("container[1]is",container[1])
container[1]=Cherries#item assignment is allowed
print("container after mutating is",container)
print("lists are MUTABLE")


