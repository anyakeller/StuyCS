class bruh:
    bruhs = 0
    
    def _init_(self,name,swagValue,isJion):
        self.name = name
        self.swagValue = swagValue
        self.isJion = isJion
        bruh.bruhs += 1
        
    def bruhtot(self):
        print "Total Employee %d" % bruh.bruhs
    
    def bruhSpecs(self):
        print "Name : ", self.name,  ", Is Jion?: ", self.isJion, ", Swag Value:", self.swagValue
        
bruh1 = bruh("Yolo McSwaggins", 77, False)
bruh2 = bruh("Jion Fairchild", 99, True)
bruh3 = bruh("Lord AKH", 82, False)

