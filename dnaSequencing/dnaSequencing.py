import os.path
#The function fileToList receives one parameter filename a string. It should return a list of the lines in the file.
#Remove the newline character from the end of each line. If the file is empty or does not exist return an empty list.
def fileToList(filename):
    if os.path.isfile(filename) == True:
        fil = open(filename)
        flist = []
        for line in fil:
            line = line.strip('\n')
            flist.append(line)
        fil.close()
        return flist
    else:
        return []

#The function returnFirstString receives one parameter strings a list of strings and returns the first string.
#If the list is empty the function should return an empty string.
def returnFirstString(strings):
    if len(strings) > 0:
        return strings[0]
    else:
        return ""

#the function strandsAreNotEmpty receives two parameters strand1 and strand2, both strings.
#It returns True if both strands have a length greater than zero, or False otherwise.
def strandsAreNotEmpty(strand1, strand2):
    return len(strand1) > 0 and len(strand2) > 0

#The function strandsAreEqualLengths receives two parameters strand1 and strand2, both strings.
#It returns True if the length of both strands are equal or False otherwise.
def strandsAreEqualLengths(strand1, strand2):
    return len(strand1) == len(strand2)

#The function cadidateOverlapsTarget receives three parameters target a string, candidate a string, and overlap an integer.
#It checks to see if the target and candidate strands have an overlap of overlap characters. The function should return True if they overlap or False otherwise.
def candidateOverlapsTarget(target, candidate, overlap):
    return target[len(target)- overlap:] == candidate[:overlap]

#The function findLargestOverlap receives two parameters target and candidate, both strings.
#It should find the largest overlap and return the size of the overlap.
#If either strand is empty or the strands are not the same length, return -1. Use the functions you have already written, strandsAreNotEmpty and strandsAreEqualLengths.
def findLargestOverlap(target, candidate):
    largest = 0
    if strandsAreNotEmpty(target, candidate) == True and strandsAreEqualLengths(target, candidate) == True:
        for i in range(len(target) + 1 ):
                if candidateOverlapsTarget(target, candidate, i) == True:
                    largest = i
        return largest
    else:
        return -1

#The function findBestCandidate receives two parameters target a string, and candidates a list of strings.
#It examines each candidate in the candidates list and determines the candidate with the largest overlap.
#You can use the function findLargestOverlap to do this. If two candidates have the same overlap keep the first one.
#The function returns a tuple containing the candidate string with the largest overlap and the overlap.
#If no candidates overlap you should return an empty string for the candidate and 0 for the overlap.
def findBestCandidate(string, candidates):
    overlap = 0
    can = ""
    for n in range(len(candidates)):
        if findLargestOverlap(string, candidates[n]) > overlap:
            overlap = findLargestOverlap(string, candidates[n])
            can = candidates[n]
    if overlap > 0:
        best = ((can), overlap)
        return best
    else:
        return ("", 0)


#The function joinTwoStrands receives three parameters target a string, candidate a string, and overlap an integer.
#It joins the target and candidate strands together merging them and returns the joined strand.
def joinTwoStrands(target, candidate, overlap):
    joined = ""
    if overlap > 0:
        joined = target[:(len(target) - overlap )] + candidate
        return joined
    else:
        return target


#The function main receives no parameters and returns nothing.
#The function should start by asking the user for the filename of the target strand file and candidate strands file (hint: use functions; fileToList, returnFirstString).
#After determining which of the candidate DNA strands is the best match (hint: use findBestCandidate), print the combined strand (hint: use joinTwoStrands).
def main():
    tarfil = input("Target strand filename: ")
    canfil = input("Candidate strands filename: ")
    tsrand = fileToList(tarfil)
    csrand = fileToList(canfil)
    bescan = findBestCandidate(tsrand, csrand)
    print(joinTwoStrands(tsrand, bescan[0], bescan[1]))


    end = input("Press any key to quit")


if __name__ == '__main__':
    main()
