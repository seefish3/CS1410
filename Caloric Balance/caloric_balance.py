class CaloricBalance:

    def __init__(self, gender, age, height, weight):
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.balance = 0.0
        

    def getBMR(self, gender, age, height, weight):
        if gender == m:
            self.balance = 66 + (12.7 * height) + (6.23 * weight) - (6.8 * age)
            #return self.balance
        elif gender == f:
            self.balance = 655 + (4.7 * height) + (4.35 * weight) - (4.7 * age)
            #return self.balance
        else:
            return 0.0
        
    def getBalance(self):
        return self.balance

    def recordActivity(self, cbppm, minutes):
        burn = minutes * (cbppm * self.weight)
        self.balance -= burn

    def eatFood(self, calories):
        self.balance += calories
        
    