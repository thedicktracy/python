# CabreraP4
# Programmer: Robert Cabrera
# EMail: rcabrera14@cnm.edu
# Purpose: This program will enable to user to translate from english to spanish 


def header():
        print("\nThis function will print a summary explaining the purpose of the program.")
        print("CabreraP4")
        print("Programmer: Robert Cabrera")
        print("EMail: rcabrera14@cnm.edu")
        print("This program will enable the user to translate from english to spanish\n")
def translate():
    spanish = {'hello': 'hola','goodbye':'adios','what\'s your name':'como te llama\n'}
    #print(spanish['what\'s your name'])
    print(spanish.keys())
    z=input("\nplease enter a phrase to translate::  ")
    if z in spanish.keys():
        print(spanish[z])
    else:
        print('\n**please enter a phrase from the dictionary**:: \n')
        translate()
def cont():
    a=input("\nwould you like to translate again? (yes/no) ::  ")    
    return a

def goodbye():
    print('\ngoodbye && adios\n')
    
def main():
    header()       
    a='yes' 
    while a == 'yes':
        translate() 
        a=cont()
        if a == 'yes':
            pass
        elif(a=='no'):
            goodbye()
            exit()
        else:
            print('\n**please type yes or no**\n')   
    
      
if __name__ == '__main__':
        main() 
 

    
