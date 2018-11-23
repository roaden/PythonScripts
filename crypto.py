options = [
           "Pick new phrase",
           "Caesar cipher",
           "Vigenere cipher",
           "Divide up",
           "Exit."]


def pickOption():
    while True:
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Must be an integer!")
            menu()
        if choice == 0:
            pickPhrase()
            return
        elif choice == 1:
            caesarCipher()
            return
        elif choice == 2:
            vigenereCipher()
            return
        elif choice == 3:
            divideUp()
            return
        elif choice == 4:
            global keepGoing
            keepGoing = False
            return
        else:
            print("Not valid choice.")
            menu()
    
    

def menu():
    print("Please choose from the following options:")
    print()
    for i in range(len(options)):
        print(str(i) + ": " + options[i])

def ashift(n, toshift):
    if len(toshift) > 1:
        print("Error, expected single character.")
        print("Only looking at first character.")
        toshift = toshift[0]
    if toshift.isupper():
        makebig = True
        toshift = toshift.lower()
    elif toshift.islower():
        makebig = False
    else:
        return toshift
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    postshift = alphabet[(alphabet.find(toshift)+n)%26]
    if makebig:
        return postshift.upper()
    else:
        return postshift
        
        
def pickPhrase():
    global thePhrase
    print("Enter phrase to work with:")
    thePhrase = input()

def caesarCipher():
    while True:
        try:
            shift = int(input("Enter number to shift by: "))
            break
        except ValueError:
            print("It's gotta be an integer, sorry!")
    while True:
        encrypting = input("Encrypting (e) or Decrypting (d)? ")
        if encrypting == 'e':
            break
        elif encrypting == 'd':
            shift = -shift
            break
        else:
            print("Must be 'e' or 'd'.")
    for i in range(len(thePhrase)):
        print(ashift(shift, thePhrase[i]), end='')
    print()

def passPhrase(foo):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    passNum = []
    if len(foo) == 0:
        passNum.append(0)
        return passNum
    for i in range(len(foo)):
        try:
            passNum.append(alphabet.index(foo[i].lower()))
        except ValueError:
            passNum.append(0)
    return passNum
            
    

def vigenereCipher():
    passNum = passPhrase(input("Enter decryption word: "))
    passNumSize = len(passNum)
    while True:
        encrypting = input("Encrypting (e) or Decrypting (d)? ")
        if encrypting == 'e':
            break
        elif encrypting == 'd':
            for i in range(len(passNum)):
                passNum[i] = -passNum[i]
            break
        else:
            print("Must be 'e' or 'd'.")
    n = 0
    for i in range(len(thePhrase)):
        print(ashift(passNum[n], thePhrase[i]), end='')
        if thePhrase[i].isalpha():
            n += 1
            n = n%passNumSize
    print()
    
    
def divideUp():
    while True:
        try:
            n = int(input("Number to split by: "))
        except ValueError:
            print("Must be an integer")
            continue
        if n <= 0:
            print("Must be a positive integer.")
        else:
            break
    for i in range(n):
        if i > len(thePhrase):
            break
        print("Line " + str(i+1) + ":")
        j = i
        while j < len(thePhrase):
            print(thePhrase[j], end='')
            j += n
        print()
    

    
keepGoing = True

pickPhrase()        

while keepGoing:
    menu()
    pickOption()