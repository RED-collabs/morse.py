import time
print("!!!!!First time user use 3\n")
#stored data :}  
dict ={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',' ':'|',
    '0': '-----', '1': '.----', '2': '..--', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

#--#
def main():
    print('''Select the menu:
\t1 For English to Morse
\t2 For Morse to English
\t3 For Help''')
    chse=input("Choose: ").upper()
    print("")
    if chse=="1":
        cov1()
    elif chse=="2":
        cov2()
    elif chse=="3":
        h()
    elif chse=="RED":
        credit()
    else:
        print("Bye[ER404]")
        time.sleep(2)
        quit()
def path():
    way=input("> ").upper()
    if way=="M":
        main()
        exit
        
    return way
def h():
    print("| this means a end of a word")
    print("you can press Enter to exit/Continue")
    print("Type RED in the main menu for credit display")
    print("Use M or m to visit ")
    input()
    main()
    
def cov1():
    print("Input the word in English")
    char=input("> ").upper()
    print()
    list=[]
    list1=[]
    for i in char:
        if i not in dict:
            print(i,"is not in the Data base")
            exit
        else:
             list1.append(i)
             list.append(dict[i])
             continue
    print("\n",*list1)
    print(*list)
    path()
    cov1()
    
def cov2():
    list2 = []
    list3 = []
    mrse=0
    print("!Use / for space, /s to stop\n")
    while mrse!="/s":
        mrse = input("Morse Code: ").lower()
        list2.append(mrse)
        if mrse=="/s":
            list2.pop()
    for morse in list2:
        if morse == "/":
            list3.append(" ") 
        else:
            for key, value in dict.items():
                if value == morse:
                    list3.append(key)
                    break            
    print(">",*list3)
    path()
    cov2()
def credit():
    print('''    RRRR   EEEE DDDD
    R   R  E    D   D
    RRRR   EEEE D   D
    R  R   E    D   D
    R   R  EEEE DDDD''')
    print("\ngithub:https://github.com/RED-collabs/morse.py.git")
    input(),main()
#--#
main()
    
