import random
import pprint


LETTERS = ("C", "D", "E", "F", "G", "A", "B")

KEYBOARDKEYS = (("B#", "C", "Dbb"),
                ("B##", "C#", "Db"),
                ("C##", "D", "Ebb"),
                ("D#", "Eb", "Fbb"),
                ("D##", "E", "Fb"),
                ("E#", "F", "Gbb"),
                ("E##", "F#", "Gb"),
                ("F##", "G", "Abb"),
                ("G#", "Ab"),
                ("G##", "A", "Bbb"),
                ("A#", "Bb"),
                ("A##", "B", "Cb"))

ALLSPELLINGS = ("B#", "C", "Dbb",
                "B##", "C#", "Db",
                "C##", "D", "Ebb",
                "D#", "Eb", "Fbb",
                "D##", "E", "Fb",
                "E#", "F", "Gbb",
                "E##", "F#", "Gb",
                "F##", "G", "Abb",
                "G#", "Ab",
                "G##", "A", "Bbb",
                "A#", "Bb",
                "A##", "B", "Cb")

INTERVALSEMITONES = {"P1": 0,
                     "m2": 1,
                     "M2": 2,
                     "m3": 3,
                     "M3": 4,
                     "P4": 5,
                     "A4": 6,
                     "D5": 6,
                     "P5": 7,
                     "m6": 8,
                     "M6": 9,
                     "m7": 10,
                     "M7": 11,
                     "P8": 12}

STARTINGROOTS = ("Cb", "C", "C#",
                 "Db", "D", "D#",
                 "Eb", "E", "E#",
                 "Fb", "F", "F#",
                 "Gb", "G", "G#",
                 "Ab", "A", "A#",
                 "Bb", "B", "B#")

TESTTYPES = ("interval", "notes")
DIRECTIONS = ("above", "below")



def intervalCalculateAnswer(intervalType, direction, root):
    """
    letter refers to just the letter with no sharps or flats.
    note refers to the exact key on the keyboard.
    spelling refers to the complete name of the note.
    """
    # letter we end up with
    lettersUp = int(intervalType[1]) -1
    if direction == DIRECTIONS[1]:
        lettersUp *= -1
    startLetter = LETTERS.index(root[0])
    finalLetterIndex = (startLetter + lettersUp) % len(LETTERS)
    finalLetter = LETTERS[finalLetterIndex]

    # current semitone position
    startNote = 0
    for note in KEYBOARDKEYS:
        if root in note:
            break
        startNote += 1
    else:
        raise NotImplementedError

    # semitones calculations
    semitonesToTraverse = INTERVALSEMITONES[intervalType]
    if direction == DIRECTIONS[1]:
        semitonesToTraverse *= -1
    newNote = (startNote + semitonesToTraverse) % len(KEYBOARDKEYS)

    # finding the answer
    for spelling in KEYBOARDKEYS[newNote]:
        if spelling[0] == finalLetter:
            return spelling
    else:
        raise NotImplementedError


def askQuestion(intervalType, direction, root, answer, testType=TESTTYPES[0]):
    if testType == TESTTYPES[0]:
        msg = "{} {} {}".format(intervalType, direction, root)
    else:
        newDirection = ""
        if direction == DIRECTIONS[0]:
            newDirection = "up to"
        else:
            newDirection = "down to"
        msg = "What interval does {} {} {} make?".format(root, direction, answer)
    print(msg)





def main():
    """ the start of the drills go here """
    runDrills()


def runDrills():
    score = 0
    totalQuestions = 0
    drillType = getDrillType()
    while True:
        print()
        if runIndividualDrill(*drillType):
            score += 1
        totalQuestions += 1
        msg = "{} / {}".format(score, totalQuestions)
        print(msg)


def getDrillType():
    msg = """
Please write the interval you want to be tested on.
The format is just "IntervalType [Direction: up/down]" """
    print(msg)
    return userInput()


def runIndividualDrill(intervalType, direction=None):
    startingRoot = random.choice(STARTINGROOTS)
    if not direction:
        direction = random.choice(DIRECTIONS)
    answer = intervalCalculateAnswer(intervalType, direction, startingRoot)
    askQuestion(intervalType, direction, startingRoot, answer)
    usrAnswer = userAnswerInput()
    if usrAnswer.lower() != answer.lower():
        print("WRONG. The correct answer is {}".format(answer))
        return False
    return True


def userInput():
    warningMsg = "Please write the interval you want to be tested on. E.g.: P5[, up/down]"
    while True:
        usrInput = input("> ")
        if usrInput.lower() == "q" or usrInput.lower() == "quit":
            quit()
        usrInput = usrInput.split()
        if (len(usrInput) == 0 or 
                usrInput[0] not in INTERVALSEMITONES or
                len(usrInput) == 2 and usrInput[1] not in DIRECTIONS):
            print(warningMsg)
            continue
        return usrInput

def userAnswerInput():
    while True:
        usrInput = input("> ")
        if usrInput == "":
            continue
        elif usrInput.lower() == "q" or usrInput.lower() == "quit":
            quit()
        elif usrInput[0].upper() + usrInput[1:].lower() not in ALLSPELLINGS:
            print("That's not a note")
            continue
        else:
            return usrInput




if __name__ == "__main__":
    main()



