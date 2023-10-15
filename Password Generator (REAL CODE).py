import string
import typing
import random as r
import dataclasses
from dataclasses import *
import cfonts
import termcolor
from termcolor import *
import sys
import time as tm
import os
import keyboard
from keyboard import *
import pyautogui
from pyautogui import *

'''           Miscellaneous Tools As Functions             '''

# Clear Function
def clear_screen():
    os_id = os.name
    
    if os_id == 'nt':
        os.system("cls")
    if os_id == 'posix':
        os.system("clear")

# Slowprint Function
def slowprint(text, speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        tm.sleep(speed)

# Removes unwanted characters from passwords (Function)
def remove_chars(string):
    # Replace ','
    string = string.replace(',', '')
    
    # Replace '[' and ']'
    string = string.replace('[', '').replace(']', '')
    
    # Remove spaces
    string = ''.join(string.split())
    
    return string

def choice_error_checking(menu_size):
    try:
        choice = int(input())
        if choice > menu_size: # If User selects option out of range
            slowprint(cfonts.render(f"Choice is out of range, please select another option.", font="console", align="center"), 1./90)
            tm.sleep(2)
            os.system("cls")
        return choice
    except ValueError:
        slowprint(cfonts.render(f"String not valid, please choose a number.", font="console", align="center"), 1./90)
        tm.sleep(2)
        os.system("cls")
        
'''         Password Generator Class and Functions          '''

# Password Generator Class
@dataclass(frozen=False)
class Password_Generator():
    letters: [] = field(default_factory = lambda: list(string.ascii_letters))
    numbers: [] = field(default_factory= lambda: str([nums for nums in range(0, 10)]))
    random_chars: [] = field(default_factory= lambda: ['!', '#', '$', '%', '&', '(', ')',
                                                       '*', '+', '-', '.', ':', ';',
                                                       '<', '=', '>', '?', '@', '^',
                                                       '_', '`', '{', '|', '}', '~'])
    
    def generate_strong_password(self): # Strong Password Generator
        pre_password = []
        
        for apperance in range(3): # Loading Message
            clear_screen()
            slowprint(cfonts.render("Generating strong password...", font="console", align="center"), 1./300)
            tm.sleep(1)
        
        for chars in range(10): # Pre-Password Generating Password Characters
            pre_password.append(r.choice(self.letters))
            pre_password.append(r.choice(self.numbers))
            pre_password.append(r.choice(self.random_chars))
            r.shuffle(pre_password) # Shuffles Pre-Password for further encryption (Randomness)
        
        strong_password = str()
        
        for char in pre_password: # 'pre-password' vonverts from being a list to a string variable 'strong_password'
            strong_password += str(char)
        
        strong_password = "".join(strong_password.split()) # Removes whitespaces in string
        while True:
            slowprint(cfonts.render(f"New Strong Password Generated:|{strong_password}", font="console", align="center"), 1./300)
            slowprint(f"{'':80}Would you like to keep it? (Y/n): ", 1./90)
            
            choice = str(input())
            
            yn_list = ['y', 'Y', 'n', 'N']
            
            if choice.isdigit():
                slowprint(cfonts.render("Numbers not allowed, please choose either|'y' or 'Y'| 'n' or 'N'.", font="console", align="center"), 1./90)
                tm.sleep(2)
                clear_screen()
            elif choice not in yn_list:
                slowprint(cfonts.render("Invalid string, please choose either:|'y' or 'Y'| 'n' or 'N'.", font="console", align="center"), 1./90)
                tm.sleep(2)
                clear_screen()
            
            match choice:
                case 'y' | 'Y': # Users chooses to save password via file
                    clear_screen()
                    
                    moving_text = "Saving Now..."
                    moving_letters = [char for char in moving_text]
                    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
                    
                    slowprint(cfonts.render(f"{moving_text}", font="console", align="center"), 1./30)
                    
                    tm.sleep(2)
                    
                    for apperance in range(4): # Moving Text For-Loop Solution
                        clear_screen()
                        
                        spaces = [r.randint(1, 10), r.randint(50, 130)]
                        
                        print('\n' * spaces[0])
                        print(' ' * spaces[1], end='')
                        for char in moving_letters: # Prints Colored 'moving_text'
                            cprint(f"{char}", r.choice(colors), end='')
                            tm.sleep(1./30)
                        tm.sleep(2)
                    
                    # Saves Password to 'password.txt'
                    file_manager = open("password.txt", 'a')
                    file_manager.write('\n')
                    file_manager.write(strong_password)
                    file_manager.close()
                    
                    clear_screen()
                    break
                
                case 'n' | 'N':
                    clear_screen()
                    slowprint(cfonts.render("Alright, deleting now...", font="console", align="center"), 1./90)
                    tm.sleep(3)
                    clear_screen()
                    break
    
    def generate_weak_password(self): # Weak Password Generator
        
        for apperance in range(3): # Loading Message
            clear_screen()
            slowprint(cfonts.render("Generating weak password...", font="console", align="center"), 1./300)
            tm.sleep(1)
        
        # Chooses Weak Password from file
        weak_password = r.choice(open("10-million-password-list-top-1000000.txt", "r").read().split())
        while True:
            slowprint(cfonts.render(f"New Weak Password Generated:|{weak_password}", font="console", align="center"), 1./300)
            slowprint(f"{'':80}Would you like to keep it? (Y/n): ", 1./90)

            choice = str(input())
            
            yn_list = ['y', 'Y', 'n', 'N']
            
            if choice.isdigit():
                slowprint(cfonts.render("Numbers not allowed, please choose either|'y' or 'Y'| 'n' or 'N'.", font="console", align="center"), 1./90)
                tm.sleep(2)
                clear_screen()
            elif choice not in yn_list:
                slowprint(cfonts.render("Invalid string, please choose either:|'y' or 'Y'| 'n' or 'N'.", font="console", align="center"), 1./90)
                tm.sleep(2)
                clear_screen()
            match choice:
                case 'y' | 'Y': # Users chooses to save password via file
                    clear_screen()
                    
                    moving_text = "Saving Now..."
                    moving_letters = [char for char in moving_text]
                    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
                    
                    slowprint(cfonts.render(f"{moving_text}", font="console", align="center"), 1./30)
                    
                    tm.sleep(2)
                    
                    for apperance in range(4): # Moving Text For-Loop Solution
                        clear_screen()
                        
                        spaces = [r.randint(1, 10), r.randint(50, 130)]
                        
                        print('\n' * spaces[0])
                        print(' ' * spaces[1], end='')
                        for char in moving_letters: # Prints Colored 'moving_text'
                            cprint(f"{char}", r.choice(colors), end='')
                            tm.sleep(1./30)
                        tm.sleep(2)
                    
                    # Saves Password to 'password.txt'
                    file_manager = open("password.txt", 'a')
                    file_manager.write('\n')
                    file_manager.write(weak_password)
                    file_manager.close()
                    
                    clear_screen()
                    break
                
                case 'n' | 'N':
                    slowprint(cfonts.render("Alright, deleting now...", font="console", align="center"), 1./90)
                    tm.sleep(3)
                    clear_screen()
                    break
            
    def custom_password(self):
        clear_screen()
        
        print("\n" * 3)
        slowprint(cfonts.render("Hello!|Please enter your custom password below:", font="console", align="center"), 1./90)
        custom_password = input(f"{'password: ':>90}")
        
        clear_screen()
        while True:
            slowprint(cfonts.render(f"Custom Password Entered:|{custom_password}", font="console", align="center"), 1./90)
            slowprint(f"{'':>85}Would you like to keep it?: ", 1./90)
            
            choice = str(input())
            
            yn_list = ['y', 'Y', 'n', 'N']
                
            if choice.isdigit():
                slowprint(cfonts.render("Numbers not allowed, please choose either|'y' or 'Y'| 'n' or 'N'.", font="console", align="center"), 1./90)
                tm.sleep(2)
                clear_screen()
            elif choice not in yn_list:
                slowprint(cfonts.render("Invalid string, please choose either:|'y' or 'Y'| 'n' or 'N'.", font="console", align="center"), 1./90)
                tm.sleep(2)
                clear_screen()
            match choice:
                case 'Y' | 'y': # Saves the password
                    clear_screen()
                    
                    moving_text = "Saving Now..."
                    moving_letters = [char for char in moving_text]
                    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
                    
                    slowprint(cfonts.render(f"{moving_text}", font="console", align="center"), 1./30)
                    
                    tm.sleep(2)
                    
                    for apperance in range(4): # Moving Text For-Loop Solution
                        clear_screen()
                        
                        spaces = [r.randint(1, 10), r.randint(50, 130)]
                        
                        print('\n' * spaces[0])
                        print(' ' * spaces[1], end='')
                        for char in moving_letters: # Prints Colored 'moving_text'
                            cprint(f"{char}", r.choice(colors), end='')
                            tm.sleep(1./30)
                        tm.sleep(2)
                    
                    # Saves Password to 'password.txt'
                    file_manager = open("password.txt", 'a')
                    file_manager.write('\n')
                    file_manager.write(custom_password)
                    file_manager.close()
                    
                    clear_screen()
                    break
                case 'N' | 'n': # Deletes Password
                    clear_screen()
                    slowprint(cfonts.render("Alright, deleting now...", font="console", align="center"), 1./90)
                    tm.sleep(3)
                    clear_screen()
                    break

'''                  Important Variables                    '''

# Password Generator Instances Variable
pass_gen = Password_Generator()

# File Manager Variable
file_manager = None

# Runtime Variable
running = True

# Choice Variable
choice = None

'''                      Main Program                        '''

# Main Loop
while running:
    clear_screen()
    if __name__ == "__main__":
        # Checking if 'password.txt' exists, else it creates the file if not found
        if os.path.exists('password.txt') == False:
            slowprint(cfonts.render("Making 'password.txt'...", font="console", align="center"), 1/90)
            tm.sleep(3)
            file_manager = open('password.txt', 'x')
            file_manager.write(f"""-----PASSWORDS-----""")
            file_manager.close()
            
            os.system("cls")
            
        # Data From 'password.txt'
        file_manager = open("password.txt", "r")                     
        file_data = file_manager.readlines()
        file_manager.close()
        
        slowprint(cfonts.render("Legacy Password Generator!", font="chrome", align="center"), 1./500)
        slowprint(cfonts.render("1. Generate Strong Password|2. Generate Weak Password|3. Create Custom Password|4. Show Passwords|5. Exit", font="console", align="center"), 1./200)
        slowprint(f"{'':>85}Please choose an option: ", 1./300)
        
        # Main Screen
        
        choice = choice_error_checking(5)
        
        match choice:
            case 1: # Strong Password Choice
                pass_gen.generate_strong_password()
            case 2: # Weak Password Choice
                pass_gen.generate_weak_password()
            case 3: # Custom Password Choice
                pass_gen.custom_password()
            case 4: # Show Passwords Choice
                clear_screen()
                
                while True: # Main Password List Menu
                    slowprint(f"{'':>85}=====PASSWORDS=====\n", 1./500)
                    for index, e in enumerate(file_data[1:]):
                        slowprint(f"{'':>85}{index + 1}. {e}", 1./500)
                    tm.sleep(1)
                    
                    slowprint(cfonts.render(f"1. Edit/Delete Password|2. Exit", font="console", align="center"), 1./90)
                    slowprint(f"{'':>85}Please choose an option: ", 1./90)
                    
                    choice = choice_error_checking(2)
                    
                    match choice:
                        case 1: # User chooses to Edit/Delete Password
                            
                            slowprint(f"{'':>85}Select a password: ", 1./200)

                            pass_choice = choice_error_checking(len(file_data)) # Retrives the password from index number in list
                            
                            if pass_choice in range(len(file_data)): # If choice is within indec range
                                clear_screen()
                                
                                selected_password = [char for char in file_data[pass_choice]] # Password from file_data is converted from string to list
                                if '\n' in selected_password: # Removes '\n' from selected_password to not automatically making a newline
                                    index = selected_password.index('\n')
                                    selected_password.pop(index)
                                
                                slowprint(cfonts.render("Edit Password Below.|To delete password, type 'delete.'", font="console", align="center"), 1./90)
                                
                                print(f"{'':>93}", end='')
                                pyautogui.typewrite(selected_password) # Types out the password to edit, a feature that took a long time to feature out.
                                                                    # Removing the '\n' was one of them
                                
                                change_password = str(input())
                                
                                if change_password == "DELETE": # Deletes Password in file
                                    slowprint(cfonts.render("Deleting now...", font="console", align="center"), 1./90)
                                    tm.sleep(3)
                                    file_data.pop(pass_choice)
                                    
                                    # Saving changes to file
                                    file_manager = open("password.txt", "w")
                                    
                                    file_manager.writelines(file_data)
                                    
                                    file_manager.close()
                                    # End
                                    
                                    clear_screen()
                                elif change_password == "QUIT": # Back to Password List Menu
                                    slowprint(cfonts.render("Quitting now...", font="console", align="center"), 1./90)
                                    tm.sleep(1)
                                    clear_screen()
                                else: # Updates Selected Password into file
                                    clear_screen()
                                    
                                    selected_password = [char for char in change_password]
                                    selected_password.append('\n')

                                    file_data[pass_choice] = "".join(selected_password)

                                    # Saving changes to file
                                    file_manager = open("password.txt", "w")
                                    
                                    file_manager.writelines(file_data)
                                    
                                    file_manager.close()
                                    # End
                        case 2: # Returns to main menu
                            clear_screen()
                            break
            case 5: # Exits Program
                sys.exit()