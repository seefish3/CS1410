import sys
#The function createIndex does not receive any parameters. It must return an empty dictionary for the index.
# this passed the test
def createIndex():
    d = {}
    return d

#The function recordBook receives three parameters, the index dictionary, the ISBN of a book, and the title of a book.
#Both the ISBN and title are strings. It must assign the title to the ISBN in the index. It does not return anything.
#However, the dictionary will be modified as a result of this function’s work.
# this passed the test
def recordBook(d, ISBN, title):
    d[ISBN] = title

#The function findBook receives two parameters, the index dictionary and the ISBN of a book.
#The ISBN is a string. The function returns the title of the book with the matching ISBN, if it exists.
#If the ISBN is not in the dictionary, then it returns the empty string.
# this passed the test
def findBook(d, ISBN):
    if ISBN in d:
        return d[ISBN]
    else:
        return ""


#The function listBooks receives one parameter, the index dictionary. The function returns a list of strings.
#Each string in the list is a line that shows a sequence number, the ISBN and the title of a book.
#See the examples for the format of the lines. If there are no books in the index, this function returns an empty list.
#passed
def listBooks(d):
    total = 0
    books = []
    for n in d:
        total +=1
        books.append(str(total) + ") "+ n + ":" + findBook(d, n) )
    return books



#The function formatMenu does not receive any parameters. It must return a list of strings that contains the lines of the menu.
def formatMenu():
    return["What would you like to do?", "[r] Record a Book", "[f] Find a Book", "[l] List all Books", "[q] Quit"]

#The function formatMenuPrompt does not receive any parameters. It must return a string that contains the prompt to ask the user which menu option they would like to select.
def formatMenuPrompt():
    prompt = "Enter an option: "
    return prompt

#The function getUserChoice receives one parameter, a string that contains a prompt for input.
#It must return a string that contains the text input by the user, with any leanding and trailing whitespace removed.
#If the user gives an empty string, prompt them again, until they give a non-empty string. Note that this function interacts with the user, so there will be output to the screen and input from the keyboard when it is called.
#passes
def getUserChoice(prompt):
    opton = input(prompt)
    opton = opton.strip()
    while len(opton) == 0:
        opton = input(prompt)
        opton = opton.strip()
    return opton

#The function getISBN does not receive any parameters. It must prompt the user for an ISBN, and return the ISBN input by the user. The user’s response must not have any leading or trailing whitespace.
#It must repeatedly ask the user for an ISBN, until the user gives a non-empty response.
#Note, you should probably call getUserChoice as part of this function.
def getISBN():
    prompt = "Enter an ISBN:"
    return getUserChoice(prompt)


#The function getTitle does not receive any parameters. It must prompt the user for a book title, and return the title input by the user.
#The user’s response must not have any leading or trailing whitespace. It must repeatedly ask the user for a title, until the user gives a non-empty response.
#Note, you should probably call getUserChoice as part of this function.
def getTitle():
    prompt = "Enter a book title:"
    return getUserChoice(prompt)

#The function recordBookAction receives the index dictionary as a parameter. It must ask the user for the ISBN and title of a book, and add it to the dictionary.
#This function does not return anything. However, it has the side effect of adding an entry to the dictionary.
#It also interacts with the user through input and output. Note you should be using some of the above functions to complete this function.
#passed
def recordBookAction(d):
    ISBN = getISBN()
    Title = getTitle()
    recordBook(d, ISBN, Title)
    print("Book saved!")


#The function findBookAction receives the index dictionary as a parameter. It must ask the user for the ISBN a book. If the book exists in the dictionary, it will display the book.
#If the book does not exist in the dictionary, it will give the user a message to let them know. The function does not return anything, and should not change the index.
# Passed
def findBookAction(d):
    prompt = "what is the ISBN of the book you are looking for"
    index = getUserChoice(prompt)
    if index in d:
        print( "book found: " + d[index])
    else:
        print("Im Sorry I could not find the book")

#The function listBooksAction receives the index dictionary as a parameter. It will display all of the books in the dictionary in the format shown in the examples.
#If there are no books in the dictionary, it must display a message to inform the user. The function does not return anything. The function must not change the dictionary.
def listBooksAction(d):
    books = listBooks(d)
    if len(books) > 0:
        for i in range(len(books)):
            print(books[i])
    else:
        print("Im sorry the index is empty")



#The function quitAction receives the index dictionary as a parameter. This function will display a message to the user indicating the end of the program.
#It will then terminate the program using sys.exit( 0 ). Be sure to do the correct import statement. This function does not return anything.
def quitAction(d):
    print("the program will now quit")
    sys.exit( 0 )
    


#The function applyAction receives the index dictionary and a choice string as parameters.
#This function will call the appropriate action function based on the choice string.
#If the choice string does not match any accepted choices, it will display a message to the user.
#This function does not return anything. The dictionary may be changed as a result of the chosen action.
#passed
def applyAction(d, choice):
    if choice == "r":
        recordBookAction(d)
    elif choice == "f":
        findBookAction(d)
    elif choice == "l":
        listBooksAction(d)  
    elif choice == "q":
        quitAction(d)
    else:
        print("bad choice")
        

def main():
    d = createIndex()
    while True:
        men = formatMenu()
        for i in men:
            print(i)
        p = getUserChoice(formatMenuPrompt())
        applyAction(d, p)


if __name__ == '__main__':
    main()
