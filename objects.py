
class bruh:
    'Bruh creatures'
    bruhs = 0
    
    def __init__(self,name,swagValue,isJion):
        self.name = name
        self.swagValue = swagValue
        self.isJion = isJion
        bruh.bruhs += 1
        
    def bruhtot(self):
        print "Total Bruhs %d" % bruh.bruhs
    
    def bruhSpecs(self):
        print "Name:", self.name,  ", Is Jion?:", self.isJion, ", Swag Value:", self.swagValue
        
bruh1 = bruh("Yolo McSwaggins", 77, False)
bruh2 = bruh("Jion Fairchild", 255*255 - 1, True)
bruh3 = bruh("Lord AKH", 82, False)

bruh1.bruhSpecs()
bruh2.bruhSpecs()
print "How many bruhs: %d" % bruh.bruhs

