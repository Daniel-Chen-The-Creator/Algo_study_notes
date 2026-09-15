#Sep 12 Notes

class person:
    def __init__(a,firstname,lastname):
        a.firstn = firstname # Meaning: assign "firstn" of "a" a value of firstname
        a.lastn = lastname
        
    def printname(a):
        print(a.firstn,a.lastn)

x = person("Daniel","Chen") #In order to initialize, put x = ...
x.printname()

#Pyhton would automatically calls the method "__init__" from class to initialize.