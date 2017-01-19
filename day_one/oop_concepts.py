#This is a class representing schools
class Schools(object):
   #Encapsulation
    def __init__(self, name, level, type):
        self.name = name #attributes
        self.level = level #attributes
        self.type = type #attributes
        
#Method same as function
    def description(self):
    ("This is %s %s and It is a %s ,%s school." % 
(self.name self.level)



#Inheritance
class PrimarySchool(Schools):
    #represents a primary school
    def __init__(self, name, type):
        PrimarySchool.__init__(self, name,level,type)
        self.fees= fees
        print("This is %s %s and It is a %s ,%s school." % 
        (self.name self.level)
 

#Inheritance and polymorphism
class SEcondarySchool(Schools):
    #represents a  SecondarySchool
    def __init__(self, name, type):
         SecondarySchool.__init__(self, name,level,type)
        self.fees= fees
        print("This is %s %s and It is a %s ,%s school." %

#This is function
    def is_expensive(self):
        if not :self.type = private
            print "This is a public school."
        else:
            print "We are funded by the government."
