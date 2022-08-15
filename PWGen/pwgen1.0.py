
import secrets
import string
from colorama import Fore, Style
import pyperclip


# Define Data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
punct = string.punctuation


# Get password length 
length = ''
while True:
  try: 
    length = int(input('\nPassword length? '))
    break
  except ValueError:    # Throw error if not number
    print(Fore.RED + "That is not a number. Try again...")
    print(Style.RESET_ALL)        


# Get selected option
# Not quite how I wanted to do this but it works fine.
while True:    
  choice = None
  choice_list = ["a", "b", "c", "q"]
  while not choice:   # Gets user choice loops through until you hit a, b or c or q to quit
     print()
     option = input("Choose type of password [A/B/C/Q]:" + Fore.GREEN + "\n A) Simple" + Fore.YELLOW + "\n B) Medium" + Fore.RED + "\n C) Crypto " + Style.RESET_ALL)
     print()
     option = option.lower()
     if option in choice_list: 
        choice  = option


# Process selected option        
  if option == "a":
    # Simple password data 
    pw = lower
    # Mix it up with Secrets magic
    password = ''.join(secrets.choice(pw) for i in range(length))  
    # Copy PW to clipboard
    pyperclip.copy(password)

    print(Fore.GREEN + 'Copied "SIMPLE" password to clipboard!')
    print(Style.RESET_ALL)

  elif option == "b":
    # Medium password data
    pw = lower + digit + upper
    # Mix it up with Secrets magic
    password = ''.join(secrets.choice(pw) for i in range(length))  
    # Copy PW to clipboard
    pyperclip.copy(password)

    print(Fore.YELLOW + 'Copied "MEDIUM" password to clipboard!')
    print(Style.RESET_ALL)

  elif option == "c":
    # Cryptop password data
    pw = lower + upper + digit + punct
    # Mix it up with Secrets magic
    password = ''.join(secrets.choice(pw) for i in range(length))  
    # Copy PW to clipboard
    pyperclip.copy(password)

    print(Fore.RED + 'Copied "CRYPTO" password to clipboard!')
    print(Style.RESET_ALL)
    
  elif option == "q":
    print(Fore.RED + 'Canceled')
    print(Style.RESET_ALL)

  break