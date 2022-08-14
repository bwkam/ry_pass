import os
import re
from curses.ascii import isalpha, isdigit
from Generator import Generator
import pyfiglet
import inflect
import sys


def main():

    if len(sys.argv) != 1: #
        print("Usage: main.py")
        print("Too many command-line arguments")
        sys.exit()

    p = inflect.engine()

    pyfiglet.print_figlet("RyPass", "larry3d")

    # Construct an object
    gen = Generator.init()
    password = gen.generate()
 

    # Some spacing
    print("\n")

    
    # Print details
    print("Password stats")
    stats = p.join((str(count_ints(password)) + " numbers" , str(count_letters(password)) + " letters", str(count_symbols(password)) + " symbols"))
    
    print(stats)

    print("\n")


    os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))


    print(f"Your password has been written to {os.getcwd()} 🎉🎉🎉\n\n")
    print("If you don't like it simply execute main.py again since it's all 'random' 😉")

    # Write it to a text file 
    # os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

    search_str = ""

    for i in os.listdir():
        search_str = search_str + " " + i


    if re.search(r"gen_passwords", search_str):
        os.chdir('gen_passwords')
        numbers = [number.split("(")[1].replace(").txt","") for number in os.listdir()]


        # Used for keep track of the most recent password generated
        greatest = 0

        for number in numbers:
            if int(number) > greatest:
                greatest = int(number)


        with open(f"password({greatest+1}).txt", "w") as file:
            file.write(password)

    else:
        os.mkdir('gen_passwords')
        os.chdir('gen_passwords')
        with open(f"password(0).txt", "w") as file:
            file.write(password)

def count_letters(gen_pass):
    letters = 0

    for i in gen_pass:
        if isalpha(i):
            letters+=1
    return letters

def count_ints(gen_pass):
    ints = 0

    for i in gen_pass:
        if isdigit(i):
            ints+=1
    return ints

def count_symbols(gen_pass):
    symbols = 0

    for i in gen_pass:
        if not isdigit(i) and not isalpha(i):
            symbols+=1
    return symbols
            
            



if __name__ == "__main__":
    main()