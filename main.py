import os
from time import sleep
try:
    from colorama import Fore, Back, Style, init
    import colorama
except:
    print("Chyba: Program potřebuje colorama. Stáhněte colorama library. Díky 'pip install colorama'")
    exit()
init()

def bsod(reason):
    print(Back.BLUE)
    for i in range(0,100,10):
        os.system("cls")
        
        print(f"""{Back.BLUE}{Fore.WHITE}
A problem has been detected and Windows has been shut down to prevent damage to your computer.                                                                                         
                                                                                                                                                                                       
If this is the first time you’ve seen this stop error screen, restart your computer. if this screen appears again, follow these steps:                                                 
                                                                                                                                                                                       
Check to make sure any new hardware or software is properly installed. I this is a new installation, ask your hardware or software manufacturer for and Windows updates you might need.
                                                                                                                                                                                       
If problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing.                                            
If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.                           
                                                                                                                                                                                       
Technical information:                                                                                                                                                                 
                                                                                                                                                                                       
*** STOP: {reason} ***                                                                                                                                                         
Restarting... {i}%                                                                                                                                                                     
""")
                
        sleep(1)
    print(Style.RESET_ALL)
    os.system("cls")



def minus(number1,number2):
    number1 = int(number1)
    number2 = int(number2)
    print(f"{Fore.GREEN}Výsledek je {Fore.YELLOW}{number1 - number2}{Fore.WHITE}")
    
def plus(number1,number2):
    number1 = int(number1)
    number2 = int(number2)
    print(f"{Fore.GREEN}Výsledek je {Fore.YELLOW}{number1 + number2}{Fore.WHITE}")
def deleno(number1,number2):
    number1 = int(number1)
    number2 = int(number2)
    print(f"{Fore.GREEN}Výsledek je {Fore.YELLOW}{number1 / number2}{Fore.WHITE}")
def krat(number1,number2):
    number1 = int(number1)
    number2 = int(number2)
    print(f"{Fore.GREEN}Výsledek je {Fore.YELLOW}{number1 * number2}{Fore.WHITE}")


















print(Fore.YELLOW + f"""
   ______      __           __      __            
  / ____/___ _/ /______  __/ /___ _/ /_____  _____
 / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
{Fore.BLUE}Udělal {Fore.LIGHTBLACK_EX}Justin Jindřich Lukes                                                  
      
{Fore.WHITE}
Vítejte v kalkulačce!""" + Fore.WHITE)
while True:
    
    number1 = input(Fore.YELLOW + "Zadej první číslo: " + Fore.WHITE)

    print(f"""{Fore.GREEN}Možné Operace{Fore.BLUE}
+ {Fore.CYAN}(Plus){Fore.BLUE}
- {Fore.CYAN}(Mínus){Fore.BLUE}
* {Fore.CYAN}(Krát){Fore.BLUE}
/ {Fore.CYAN}(Děleno){Fore.BLUE}
M {Fore.CYAN}(Mocniny){Fore.BLUE}
O {Fore.CYAN}(Odmocniny){Fore.BLUE}
{Fore.RED}'End' nebo 'Konec' (Pro ukončení)
{Back.BLUE}{Fore.BLACK}[?] coming soon...{Style.RESET_ALL}
    """)

    operace = input(Fore.YELLOW + "Operace: " + Fore.WHITE)
    while True:
        if operace == "End" or operace == "Konec":
            print(f"{Fore.GREEN}Děkuji moc za používání kalkulačky")
            exit()
        elif operace == "+":
            number2 = input(Fore.YELLOW + "Zadej druhé číslo: " + Fore.WHITE)
            plus(number1,number2)
            break
        elif operace == "-":
            number2 = input(Fore.YELLOW + "Zadej druhé číslo: " + Fore.WHITE)
            minus(number1,number2)
            break
        elif operace == "/":
            number2 = input(Fore.YELLOW + "Zadej druhé číslo: " + Fore.WHITE)
            if not number1 == 0 or not number2 == 0:
                deleno(number1, number2)
                break
            else:
                bsod("Nemužeš dělit nulou")
                break
        elif operace == "*":
            number2 = input(Fore.YELLOW + "Zadej druhé číslo: " + Fore.WHITE)
            krat(number1,number2)
            break
        elif operace == "M":
            number1 = int(number1)
            print(f"{Fore.GREEN}Výsledek je {Fore.YELLOW}{number1 * number1}{Fore.WHITE}")
            break
        elif operace == "O":
            number1 = int(number1)
            print(f"{Fore.GREEN}Výsledek je {Fore.YELLOW}{number1 ** (1/2)}{Fore.WHITE}")
            break
        else:
            bsod("Bad Command")
            break
