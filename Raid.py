import os
import sys
import keyboard
import time
import ctypes

# This forces the script to use the "Classic" console which supports resizing
if sys.platform == 'win32':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b): return a / b

def run_math_engine():
    # SET TITLE ONCE
    os.system('title Math Engine V1.0')
    
    while True:
        # CLEAR SCREEN
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Centering the Menu
        print("\n" * 2) # Top padding
        print("========================================".center(50))
        print("          MATH ENGINE LOADED            ".center(50))
        print("========================================".center(50))
        print(" [A] Addition".center(50))
        print(" [S] Subtraction".center(50))
        print(" [M] Multiplication".center(50))
        print(" [D] Division".center(50))
        print(" [Q] Quit".center(50))
        print("========================================".center(50))

        # Wait for a key press
        event = keyboard.read_event(suppress=True)
        
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name.lower()

            # Handling Addition
            if key == 'a':
                print("\n" + "--- ADDITION MODE ---".center(50))
                try:
                    num1 = float(input("        Enter 1st number: "))
                    num2 = float(input("        Enter 2nd number: "))
                    result_text = f"Result: {num1} + {num2} = {add(num1, num2):.2f}"
                    print("\n" + result_text.center(50))
                except:
                    print(" [!] Please enter numbers only.".center(50))
                input("\n" + "Press Enter to return to menu...".center(50))

            # Handling Subtraction
            elif key == 's':
                print("\n" + "--- SUBTRACTION MODE ---".center(50))
                try:
                    num1 = float(input("        Enter 1st number: "))
                    num2 = float(input("        Enter 2nd number: "))
                    result_text = f"Result: {num1} - {num2} = {subtract(num1, num2):.2f}"
                    print("\n" + result_text.center(50))
                except:
                    print(" [!] Please enter numbers only.".center(50))
                input("\n" + "Press Enter to return to menu...".center(50))

            # Handling Multiplication
            elif key == 'm':
                print("\n" + "--- MULTIPLICATION MODE ---".center(50))
                try:
                    num1 = float(input("        Enter 1st number: "))
                    num2 = float(input("        Enter 2nd number: "))
                    result_text = f"Result: {num1} x {num2} = {multiplication(num1, num2):.2f}"
                    print("\n" + result_text.center(50))
                except:
                    print(" [!] Please enter numbers only.".center(50))
                input("\n" + "Press Enter to return to menu...".center(50))

            # Handling Division
            elif key == 'd':
                print("\n" + "--- DIVISION MODE ---".center(50))
                try:
                    num1 = float(input("        Enter 1st number: "))
                    num2 = float(input("        Enter 2nd number: "))
                    result_text = f"Result: {num1} / {num2} = {division(num1, num2):.2f}"
                    print("\n" + result_text.center(50))
                except ZeroDivisionError:
                    print(" [!] Error: Cannot divide by zero!".center(50))
                except:
                    print(" [!] Please enter numbers only.".center(50))
                input("\n" + "Press Enter to return to menu...".center(50))

            # Exit
            elif key == 'q':
                print("\n" + "Shutting down Engine...".center(50))
                time.sleep(1)
                break

            time.sleep(0.2)

if __name__ == "__main__":
    # 1. Try to resize the physical window
    os.system('mode con: cols=50 lines=22')
    
    # 2. Force the internal "buffer" to match so text doesn't drift
    if os.name == 'nt':
        os.system(f'powershell -command "&{{$H=get-host;$W=$H.ui.rawui;$B=$W.buffersize;$B.width=50;$B.height=22;$W.buffersize=$B;}}"')
    
    run_math_engine()