#Import colouroma and Ranodm library
import random
from colorama import init, Fore, Style
init(autoreset=True)

 #Create random function 
def rand():
    options = ["🪨","📄","✂️"]
    score = 0
    robot_response = random.choice(options)
    user_response = input(f"{Fore.LIGHTCYAN_EX}Enter one(r/sc/p)").lower()
    if user_response == "r":
        if robot_response == "🪨":
            print("🪨 and 🪨")
            print(f"{Fore.YELLOW}Draw")
        elif robot_response == "📄":
                    print("🪨 and 📄")
                    print(f"{Fore.RED}Lost")
        elif robot_response == "✂️":
                    print("🪨 and 📄")
                    print(f"{Fore.LIGHTGREEN_EX}Win")
                    score = score + 1
                    print("SCORE :",score)
    elif user_response == "sc":
            if robot_response == "🪨":
                print("🪨 and ✂️")
                print(f"{Fore.RED}Lost")
            elif robot_response == "📄":
                        print("✂️ and 📄")
                        print(f"{Fore.LIGHTGREEN_EX}Win")
                        score = score + 1
                        print("SCORE :",score)
            elif robot_response == "✂️":
                        print("✂️ and ✂️")
                        print(f"{Fore.YELLOW}Draw")
    elif user_response == "p":
                if robot_response == "🪨":
                    print("🪨 and 📄")
                    print(f"{Fore.LIGHTGREEN_EX}Win")
                    score = score + 1
                    print("SCORE :",score)
                elif robot_response == "📄":
                            print("📄 and 📄")
                            print(f"{Fore.YELLOW}Draw")
                elif robot_response == "✂️":
                            print("✂️ and 📄")
                            print(f"{Fore.RED}Lost")

while True:
        print(f"{Fore.LIGHTYELLOW_EX}This is a game of rock paper scissors shoot, Do you wan to play?")
        yes_or_no = input(f"{Fore.LIGHTGREEN_EX}You:  ")
        if yes_or_no == "yes":
                rand()
        elif yes_or_no == "no":
             exit
        else:
            print("Error")