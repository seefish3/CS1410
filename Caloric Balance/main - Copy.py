import caloric_balance
import sys
#
    def formatMenu():
        return ["What would you like to do?", "[f] Record Food Consumption", "[a] Record Physical Activity", "[q] Quit"]

    #
    def formatMenuPrompt():
    prompt = "Enter an option: "
    return getUserString(prompt)

    #
    def formatActivityMenu():
        return ["What activity would you like to do?", "[j] Jump rope", "[s] Sitting", "[w] Walking", "[r] Running"]

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
    def createCaloricBalance():
        print("Hi! This program will calculate your caloric balance for the day!" '/n' "Before we can start, I need some information about you. Be honest! :) ")
        gender = getUserString("What is your gender (f or m)? ")
        age = getUserFloat("What is your age? " )
        hight = getUserFloat("What is your height in inches? ")
        wight = getUserFloat("What is your weight in pounds? ")
        cb = CaloricBalance(gender, age, height, weight)
        return cb

    #
    def recordActivityAction(cb):
        print(formatActivityMenu())
        act = getUserString("chose an activity: ")
        nac = getUserFloat( "number of minutes of activity: ")
        if act == "j":
            cbppm = .074
        elif act == "r":
            cbppm = .087
        elif act == "s":
            cbppm = .009
        elif act == "w":
            cbppm = .036
        else:
            print("that is not a valid activity")
            return
        
        return cb.recordActivity(cbppm, minutes)

    #
    def eatFoodAction(cb):
        calories = getUserFloat("enter the number of calories consumed: ")
        return cb.eatFood(calories)

    #
    def quitAction(d):
        print("the program will now quit")
        sys.exit( 0 )

    #
    def applyAction(d, choice):
        if choice == "f":
            eatFoodAction(d)
        elif choice == "a":
            recordActivityAction(d)
        elif choice == "q":
            quitAction(d)
        else:
            print("bad choice")


    #
    def main():
        cb = createCaloricBalance()
        

    if __name__ == '__main__':
        main()
