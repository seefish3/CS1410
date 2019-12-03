import sys

#passed
def milesPerGallon(miles, gallons):
    if gallons == 0:
        return 0.0
    else:
        return miles / gallons

#passed
def createNotebook():
    return []

#passed
def recordTrip(notebook, date, miles, gallons):
    d = {"date": date, "miles": miles, "gallons": gallons}
    notebook.append(d)

#Passed
def listTrips(notebook):
    trips = []
    for d in notebook:
        trips.append( "On " + str(d["date"]) + " " + str(d["miles"]) + " miles traveled using " + str(d["gallons"]) + " gallons. Gas mileage:" + str(milesPerGallon( d["miles"], d["gallons"] ))+ " MPG")
    return trips

#
def calculateMPG(notebook):
    avrage = 0.0
    tm = 0.0
    tg = 0.0
    if len(notebook) > 0:
        for d in notebook:
            tm += d["miles"]
            tg += d["gallons"]
        if tg > 0 and tm > 0:
            return tm / tg
        else:
            return 0.0
    else:
        return 0.0
#
def formatMenu():
    return['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']
    
#
def formatMenuPrompt():
    prompt = "Enter an option: "
    return prompt
#
def getUserString(prompt):
    opton = input(prompt)
    opton = opton.strip()
    while len(opton) == 0:
        opton = input(prompt)
        opton = opton.strip()
    return opton
#
def getUserFloat(prompt):
    string = 0
    while True:
        string = getUserString(prompt)
        try:
            x = float(string)
            if x > 0:
                return x
        except ValueError:
            print("you can't convert that string to a float")
            string = 0
    
#
def getDate():
    prompt = 'Input the Date: '
    return getUserString(prompt)

#
def getMiles():
    prompt = 'Input the amount of miles you travled: '
    return getUserFloat(prompt)

#
def getGallons():
    prompt = 'Input the gallons of gas: '
    return getUserFloat(prompt)

#
def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    recordTrip(notebook, date, miles, gallons)
    print("Trip Saved")
    
#
def noeempy(n):
    if len(n) > 0:
        return True
    else:
        print("there are no trips in the notebook")

#passes
def listTripsAction(n):
    l = listTrips(n)
    if noeempy(n) == True:
        for i in range(len(l)):
            print(l[i])
    else:
        print("there are no trips in the notebook")
        
    
#
def calculateMPGAction(notebook):
    g= calculateMPG(notebook)
    if noeempy(notebook) == True:
        print("Your average MPG was: " + str(calculateMPG(notebook)))
    else:
        print("There are no Trips Recorded")
    
#
def quitAction(d):
    print("the program will now quit")
    sys.exit( 0 )
    pass
#
def applyAction(notebook, choice):
    if choice == "r":
        recordTripAction(notebook)
    elif choice == "l":
        listTripsAction(notebook)
    elif choice == "c":
        calculateMPGAction(notebook)
    elif choice == "q":
        quitAction(notebook)
    else:
        print("bad choice")
#

def main():
    n = createNotebook()
    while True:
        men = formatMenu()
        for i in men:
            print(i)
        p = getUserString(formatMenuPrompt())
        applyAction(n, p)

if __name__ == '__main__':
    main()
